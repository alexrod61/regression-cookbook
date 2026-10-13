from pathlib import Path
import os
import sys
import tempfile

import numpy as np
import pandas as pd


CACHE_ROOT = Path(tempfile.gettempdir()) / "regression-cookbook-cache"
MPLCONFIGDIR = CACHE_ROOT / "matplotlib"
FONTCONFIG_CACHE = CACHE_ROOT / "fontconfig"
MPLCONFIGDIR.mkdir(parents=True, exist_ok=True)
FONTCONFIG_CACHE.mkdir(parents=True, exist_ok=True)
os.environ["XDG_CACHE_HOME"] = str(CACHE_ROOT)
os.environ["MPLCONFIGDIR"] = str(MPLCONFIGDIR)
if "--no-show" in sys.argv:
    os.environ["MPLBACKEND"] = "Agg"

import matplotlib

if "--no-show" in sys.argv:
    matplotlib.use("Agg")
import matplotlib.pyplot as plt


SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = SCRIPT_DIR / "problem-1-data.csv"
SEED = 512
N_SHIFTS = 1100

DAY_LEVELS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
MEAL_PERIOD_LEVELS = ["Brunch", "Lunch", "Dinner"]
WEATHER_LEVELS = ["Clear", "Cloudy", "Rain", "Heat"]
PALETTE = {
    "Brunch": "#009E73",
    "Lunch": "#0072B2",
    "Dinner": "#D55E00",
    "No": "#999999",
    "Yes": "#CC79A7",
    "Clear": "#0072B2",
    "Cloudy": "#999999",
    "Rain": "#56B4E9",
    "Heat": "#D55E00",
}


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def gaussian_bump(x, center, width):
    return np.exp(-0.5 * ((x - center) / width) ** 2)


def make_dataset(n_shifts=N_SHIFTS, seed=SEED):
    rng = np.random.default_rng(seed)

    day_of_week = rng.choice(
        DAY_LEVELS,
        size=n_shifts,
        p=[0.12, 0.12, 0.13, 0.14, 0.17, 0.18, 0.14],
    )
    weekend = np.isin(day_of_week, ["Saturday", "Sunday"])

    meal_period = rng.choice(
        MEAL_PERIOD_LEVELS,
        size=n_shifts,
        p=[0.18, 0.38, 0.44],
    )
    meal_period[~weekend & (meal_period == "Brunch")] = "Lunch"

    week_of_year = rng.integers(1, 53, size=n_shifts)
    seasonal_temperature = 63 + 17 * np.sin(2 * np.pi * (week_of_year - 15) / 52)
    temperature_f = seasonal_temperature + rng.normal(0, 7.5, size=n_shifts)
    temperature_f = np.clip(temperature_f, 35, 103)

    rain_probability = sigmoid(3.0 - 0.055 * temperature_f)
    heat_probability = sigmoid((temperature_f - 86) / 4.5)
    u = rng.random(n_shifts)
    weather = np.where(
        u < heat_probability * 0.45,
        "Heat",
        np.where(
            u < heat_probability * 0.45 + rain_probability * 0.50,
            "Rain",
            np.where(rng.random(n_shifts) < 0.42, "Cloudy", "Clear"),
        ),
    )

    patio_probability = sigmoid(
        -6.0
        + 0.095 * temperature_f
        + 0.35 * (weather == "Clear")
        - 1.05 * (weather == "Rain")
        - 2.05 * (weather == "Heat")
        + rng.normal(0, 0.45, size=n_shifts)
    )
    patio_open = rng.binomial(1, patio_probability, size=n_shifts)

    hour = np.empty(n_shifts)
    hour[meal_period == "Brunch"] = rng.normal(10.9, 0.75, size=(meal_period == "Brunch").sum())
    hour[meal_period == "Lunch"] = rng.normal(12.8, 0.85, size=(meal_period == "Lunch").sum())
    hour[meal_period == "Dinner"] = rng.normal(19.1, 1.05, size=(meal_period == "Dinner").sum())
    hour = np.clip(hour, 9.5, 22.5)

    day_effect = np.select(
        [
            day_of_week == "Monday",
            day_of_week == "Tuesday",
            day_of_week == "Wednesday",
            day_of_week == "Thursday",
            day_of_week == "Friday",
            day_of_week == "Saturday",
            day_of_week == "Sunday",
        ],
        [-0.35, -0.22, -0.10, 0.05, 0.38, 0.48, 0.10],
    )
    period_effect = np.select(
        [
            meal_period == "Brunch",
            meal_period == "Lunch",
            meal_period == "Dinner",
        ],
        [0.05, -0.05, 0.38],
    )

    event_probability = sigmoid(
        -2.25
        + 1.10 * (day_of_week == "Friday")
        + 1.35 * (day_of_week == "Saturday")
        + 0.45 * (meal_period == "Dinner")
        + 0.20 * np.sin(2 * np.pi * week_of_year / 13)
    )
    local_event = rng.binomial(1, event_probability, size=n_shifts)

    expected_reservations = np.exp(
        2.35
        + 0.42 * (meal_period == "Dinner")
        + 0.28 * weekend
        + 0.45 * local_event
        + 0.10 * np.cos(2 * np.pi * week_of_year / 52)
    )
    reservation_count = rng.poisson(expected_reservations)
    reservation_count = np.clip(reservation_count, 0, 85)

    staff_mean = (
        5.0
        + 0.070 * reservation_count
        + 1.6 * (meal_period == "Dinner")
        + 0.7 * weekend
        + rng.normal(0, 0.85, size=n_shifts)
    )
    staff_count = np.clip(np.rint(staff_mean), 3, 16).astype(int)

    discount_probability = sigmoid(
        -0.15
        - 0.25 * weekend
        - 0.15 * (meal_period == "Dinner")
        + 0.38 * (day_of_week == "Monday")
        + 0.28 * (day_of_week == "Tuesday")
    )
    has_discount = rng.binomial(1, discount_probability, size=n_shifts)
    discount_percent = has_discount * rng.choice(
        [5, 10, 15, 20, 25, 30],
        size=n_shifts,
        p=[0.10, 0.14, 0.18, 0.20, 0.19, 0.19],
    )

    lunch_peak = gaussian_bump(hour, center=12.7, width=0.95)
    dinner_peak = gaussian_bump(hour, center=19.2, width=1.20)
    brunch_peak = gaussian_bump(hour, center=10.9, width=0.85)
    ideal_weather = gaussian_bump(temperature_f, center=72, width=12)
    reservation_saturation = 1 - np.exp(-reservation_count / 27)
    staffing_balance = -0.020 * (staff_count - (5.8 + 0.08 * reservation_count)) ** 2
    discount_curve = 0.052 * discount_percent + 0.00025 * discount_percent**2
    weather_effect = (
        0.18 * (weather == "Clear")
        - 0.05 * (weather == "Cloudy")
        - 0.85 * (weather == "Rain")
        - 0.55 * (weather == "Heat")
    )
    patio_effect = patio_open * (
        0.55
        + 0.65 * ideal_weather
        + 0.20 * (weather == "Clear")
        - 0.10 * (weather == "Rain")
        - 0.05 * (weather == "Heat")
    )

    eta = (
        -1.30
        + day_effect
        + period_effect
        + 0.58 * lunch_peak
        + 0.88 * dinner_peak
        + 0.32 * brunch_peak
        + 1.55 * reservation_saturation
        + 0.43 * local_event
        + weather_effect
        + patio_effect
        + discount_curve
        + staffing_balance
        + 0.13 * np.sin(2 * np.pi * week_of_year / 52)
        + rng.normal(0, 0.20, size=n_shifts)
    )

    mean_occupancy = np.clip(sigmoid(eta), 0.035, 0.965)
    precision = 50 + 12 * reservation_saturation + 8 * local_event
    alpha = mean_occupancy * precision
    beta = (1 - mean_occupancy) * precision
    occupancy_rate = rng.beta(alpha, beta)
    occupancy_rate = np.clip(occupancy_rate, 0.01, 0.99)

    data = pd.DataFrame(
        {
            "occupancy_rate": np.round(occupancy_rate, 4),
            "day_of_week": pd.Categorical(day_of_week, categories=DAY_LEVELS),
            "meal_period": pd.Categorical(meal_period, categories=MEAL_PERIOD_LEVELS),
            "hour": np.round(hour, 2),
            "week_of_year": week_of_year,
            "weather": pd.Categorical(weather, categories=WEATHER_LEVELS),
            "temperature_f": np.round(temperature_f, 1),
            "patio_open": np.where(patio_open == 1, "Yes", "No"),
            "local_event": np.where(local_event == 1, "Yes", "No"),
            "reservation_count": reservation_count,
            "staff_count": staff_count,
            "discount_percent": discount_percent,
        }
    )

    missing_reservations = rng.random(n_shifts) < 0.018
    missing_weather = rng.random(n_shifts) < 0.015
    data.loc[missing_reservations, "reservation_count"] = np.nan
    data.loc[missing_weather, "weather"] = np.nan

    return data


def configure_plots():
    plt.rcParams.update(
        {
            "font.size": 15,
            "axes.titlesize": 15,
            "axes.labelsize": 15,
            "xtick.labelsize": 15,
            "ytick.labelsize": 15,
            "legend.fontsize": 15,
            "legend.title_fontsize": 15,
        }
    )


def plot_occupancy_distribution(data):
    fig = plt.figure(figsize=(8, 5), dpi=100)
    ax = fig.add_subplot(111)
    ax.hist(data["occupancy_rate"], bins=28, color="#0072B2", edgecolor="white")
    ax.set_title("Distribution of Restaurant Occupancy Rate")
    ax.set_xlabel("Occupancy rate")
    ax.set_ylabel("Number of shifts")
    ax.set_xlim(0, 1)
    fig.tight_layout()
    plt.savefig("occupancy_rate_distribution.png", bbox_inches="tight")


def plot_hourly_patterns(data):
    fig = plt.figure(figsize=(9, 5), dpi=300)
    ax = fig.add_subplot(111)

    for period in MEAL_PERIOD_LEVELS:
        period_data = data.loc[data["meal_period"] == period].copy()
        ax.scatter(
            period_data["hour"],
            period_data["occupancy_rate"],
            s=14,
            alpha=0.22,
            color=PALETTE[period],
        )

        bins = np.linspace(period_data["hour"].min(), period_data["hour"].max(), 8)
        period_data["hour_bin"] = pd.cut(period_data["hour"], bins=bins, include_lowest=True)
        trend = period_data.groupby("hour_bin", observed=True)["occupancy_rate"].mean()
        centers = np.array([interval.mid for interval in trend.index])
        ax.plot(
            centers,
            trend.values,
            marker="o",
            linewidth=2.5,
            label=period,
            color=PALETTE[period],
        )

    ax.set_title("Occupancy Rate by Time of Day")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Occupancy rate")
    ax.set_ylim(0, 1)
    ax.legend(title="Meal period", loc="upper center", bbox_to_anchor=(0.5, -0.20), ncol=3)
    fig.tight_layout()
    plt.savefig("occupancy_rate_by_hour.png", bbox_inches="tight")


def plot_reservations_by_event(data):
    clean_data = data.dropna(subset=["reservation_count"]).copy()
    bins = np.arange(0, 91, 10)

    fig = plt.figure(figsize=(9, 5), dpi=300)
    ax = fig.add_subplot(111)
    for event_status in ["No", "Yes"]:
        event_data = clean_data.loc[clean_data["local_event"] == event_status].copy()
        event_data["reservation_bin"] = pd.cut(
            event_data["reservation_count"],
            bins=bins,
            include_lowest=True,
        )
        trend = event_data.groupby("reservation_bin", observed=True)["occupancy_rate"].mean()
        centers = np.array([interval.mid for interval in trend.index])
        ax.plot(
            centers,
            trend.values,
            marker="o",
            linewidth=2.5,
            label=event_status,
            color=PALETTE[event_status],
        )

    ax.set_title("Occupancy Rate by Reservations and Events")
    ax.set_xlabel("Reservation count")
    ax.set_ylabel("Mean occupancy rate")
    ax.set_ylim(0, 1)
    ax.legend(title="Local event", loc="lower right")
    fig.tight_layout()
    plt.savefig("occupancy_rate_by_reservations_event.png", bbox_inches="tight")


def plot_weather_patio_patterns(data):
    clean_data = data.dropna(subset=["weather"]).copy()
    groups = []
    labels = []
    colors = []

    for weather in WEATHER_LEVELS:
        for patio in ["No", "Yes"]:
            values = clean_data.loc[
                (clean_data["weather"] == weather) & (clean_data["patio_open"] == patio),
                "occupancy_rate",
            ]
            if len(values) == 0:
                continue
            groups.append(values)
            labels.append(f"{weather}\n{patio}")
            colors.append(PALETTE[weather] if patio == "Yes" else "#BBBBBB")

    fig = plt.figure(figsize=(10, 5), dpi=300)
    ax = fig.add_subplot(111)
    box = ax.boxplot(groups, tick_labels=labels, patch_artist=True)
    for patch, color in zip(box["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.72)
    ax.set_title("Occupancy Rate by Weather and Patio Status")
    ax.set_xlabel("Weather and patio open")
    ax.set_ylabel("Occupancy rate")
    ax.set_ylim(0, 1)
    fig.tight_layout()
    plt.savefig("occupancy_rate_by_weather_patio.png", bbox_inches="tight")


def plot_discount_pattern(data):
    clean_data = data.copy()
    trend = clean_data.groupby("discount_percent", observed=True)["occupancy_rate"].mean()

    fig = plt.figure(figsize=(8, 5), dpi=300)
    ax = fig.add_subplot(111)
    ax.scatter(
        clean_data["discount_percent"],
        clean_data["occupancy_rate"],
        s=14,
        alpha=0.20,
        color="#999999",
    )
    ax.plot(
        trend.index,
        trend.values,
        marker="o",
        linewidth=2.5,
        color="#D55E00",
    )
    ax.set_title("Occupancy Rate by Discount Size")
    ax.set_xlabel("Discount percent")
    ax.set_ylabel("Occupancy rate")
    ax.set_ylim(0, 1)
    fig.tight_layout()
    plt.savefig("occupancy_rate_by_discount.png", bbox_inches="tight")


def main():
    configure_plots()
    os.chdir(SCRIPT_DIR)

    data = make_dataset()
    data.to_csv(OUTPUT_PATH, index=False)

    print(f"Wrote {len(data)} rows to {OUTPUT_PATH}")
    print("\nOccupancy rate summary:")
    print(data["occupancy_rate"].describe())
    print("\nMissing values:")
    print(data.isna().sum())

    plot_occupancy_distribution(data)
    plot_hourly_patterns(data)
    plot_reservations_by_event(data)
    plot_weather_patio_patterns(data)
    plot_discount_pattern(data)

    if "--no-show" in sys.argv:
        plt.close("all")
    else:
        plt.show()


if __name__ == "__main__":
    main()
