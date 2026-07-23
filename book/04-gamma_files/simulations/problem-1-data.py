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
SEED = 4161
N_ORDERS = 900

TRAFFIC_LEVELS = ["Low", "Medium", "High"]
WEATHER_LEVELS = ["Clear", "Light_Rain", "Heavy_Rain"]
PALETTE = {
    "Low": "#009E73",
    "Medium": "#E69F00",
    "High": "#D55E00",
    "Clear": "#0072B2",
    "Light_Rain": "#56B4E9",
    "Heavy_Rain": "#CC79A7",
}


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def gaussian_bump(x, center, width):
    return np.exp(-0.5 * ((x - center) / width) ** 2)


def make_dataset(n_orders=N_ORDERS, seed=SEED):
    rng = np.random.default_rng(seed)

    time_of_day = rng.uniform(10, 23, size=n_orders)
    dinner_peak = gaussian_bump(time_of_day, center=18.5, width=1.7)
    lunch_peak = gaussian_bump(time_of_day, center=12.5, width=1.1)

    is_weekend = rng.binomial(1, sigmoid(-0.65 + 0.35 * dinner_peak), size=n_orders)

    distance_km = rng.lognormal(mean=1.25, sigma=0.55, size=n_orders)
    long_trip = rng.random(n_orders) < 0.14
    distance_km[long_trip] += rng.gamma(shape=2.0, scale=1.7, size=long_trip.sum())
    distance_km = np.clip(distance_km, 0.4, 17.5)

    order_items = rng.poisson(
        2.2 + 0.65 * dinner_peak + 0.25 * is_weekend,
        size=n_orders,
    ) + 1
    order_items = np.clip(order_items, 1, 10)

    rain_score = rng.normal(-0.55 + 0.30 * is_weekend + 0.25 * np.sin(time_of_day / 2.8), 0.95)
    weather = np.where(
        rain_score > 1.05,
        "Heavy_Rain",
        np.where(rain_score > 0.18, "Light_Rain", "Clear"),
    )

    busyness = (
        34
        + 33 * dinner_peak
        + 14 * lunch_peak
        + 6 * is_weekend
        + 2.0 * order_items
        + rng.normal(0, 10, size=n_orders)
    )
    restaurant_busyness = np.clip(busyness, 5, 100)

    traffic_score = (
        -0.40
        + 1.15 * dinner_peak
        + 0.42 * lunch_peak
        + 0.12 * distance_km
        - 0.30 * is_weekend
        + 0.55 * (weather == "Heavy_Rain")
        + 0.24 * (weather == "Light_Rain")
        + rng.normal(0, 0.65, size=n_orders)
    )
    traffic_level = np.where(
        traffic_score > 1.05,
        "High",
        np.where(traffic_score > 0.25, "Medium", "Low"),
    )

    driver_experience_months = rng.gamma(shape=2.2, scale=7.5, size=n_orders)
    driver_experience_months += rng.normal(0, 2.5, size=n_orders)
    driver_experience_months = np.clip(driver_experience_months, 0, 72)

    distance_z = (distance_km - distance_km.mean()) / distance_km.std()
    busyness_z = (restaurant_busyness - restaurant_busyness.mean()) / restaurant_busyness.std()
    experience_scaled = np.log1p(driver_experience_months) / np.log(73)

    traffic_effect = (
        0.00 * (traffic_level == "Low")
        + 0.10 * (traffic_level == "Medium")
        + 0.25 * (traffic_level == "High")
    )
    weather_effect = (
        0.00 * (weather == "Clear")
        + 0.08 * (weather == "Light_Rain")
        + 0.19 * (weather == "Heavy_Rain")
    )

    log_mean_time = (
        2.65
        + 0.075 * distance_km
        + 0.0038 * restaurant_busyness
        + 0.030 * order_items
        + traffic_effect
        + weather_effect
        - 0.18 * experience_scaled
        + 0.07 * dinner_peak
        - 0.05 * is_weekend
        + 0.022 * distance_z**2
        + 0.030 * busyness_z**2
        + 0.035 * distance_z * (traffic_level == "High")
        + 0.025 * np.sin(time_of_day * np.pi / 6)
    )

    mean_time = np.exp(log_mean_time)
    delivery_time = rng.gamma(shape=8.5, scale=mean_time / 8.5)

    late_order_prob = sigmoid(
        -3.2
        + 0.55 * (traffic_level == "High")
        + 0.55 * (weather == "Heavy_Rain")
        + 0.35 * (restaurant_busyness > 78)
        + 0.08 * distance_km
    )
    late_order = rng.binomial(1, late_order_prob, size=n_orders)
    delivery_time += late_order * rng.gamma(shape=2.0, scale=4.5, size=n_orders)
    delivery_time = np.clip(delivery_time, 7, 125)

    data = pd.DataFrame(
        {
            "delivery_time_minutes": np.round(delivery_time, 1),
            "distance_km": np.round(distance_km, 2),
            "order_items": order_items.astype(int),
            "restaurant_busyness": np.round(restaurant_busyness, 1),
            "time_of_day": np.round(time_of_day, 2),
            "traffic_level": pd.Categorical(traffic_level, categories=TRAFFIC_LEVELS),
            "weather": pd.Categorical(weather, categories=WEATHER_LEVELS),
            "is_weekend": np.where(is_weekend == 1, "Yes", "No"),
            "driver_experience_months": np.round(driver_experience_months, 1),
        }
    )

    missing_busyness = rng.random(n_orders) < 0.018
    missing_experience = rng.random(n_orders) < 0.022
    data.loc[missing_busyness, "restaurant_busyness"] = np.nan
    data.loc[missing_experience, "driver_experience_months"] = np.nan

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


def plot_delivery_time_distribution(data):
    fig = plt.figure(figsize=(8, 5), dpi=300)
    ax = fig.add_subplot(111)
    ax.hist(data["delivery_time_minutes"], bins=32, color="#0072B2", edgecolor="white")
    ax.axvline(data["delivery_time_minutes"].mean(), color="#D55E00", linestyle="--", linewidth=2)
    ax.set_title("Distribution of Food Delivery Time")
    ax.set_xlabel("Delivery time, minutes")
    ax.set_ylabel("Number of orders")
    fig.tight_layout()
    plt.savefig(SCRIPT_DIR / "delivery_time_distribution.png", bbox_inches="tight")


def plot_distance_relationship(data):
    clean_data = data.dropna(subset=["distance_km", "delivery_time_minutes"]).copy()
    bins = np.linspace(clean_data["distance_km"].min(), clean_data["distance_km"].max(), 11)
    clean_data["distance_bin"] = pd.cut(clean_data["distance_km"], bins=bins, include_lowest=True)
    binned = clean_data.groupby("distance_bin", observed=True).agg(
        distance_mid=("distance_km", "mean"),
        mean_time=("delivery_time_minutes", "mean"),
    )

    fig = plt.figure(figsize=(8, 5), dpi=300)
    ax = fig.add_subplot(111)
    ax.scatter(
        clean_data["distance_km"],
        clean_data["delivery_time_minutes"],
        color="#999999",
        alpha=0.30,
        s=18,
        label="Orders",
    )
    ax.plot(
        binned["distance_mid"],
        binned["mean_time"],
        color="#D55E00",
        marker="o",
        linewidth=2.5,
        label="Binned mean",
    )
    ax.set_title("Delivery Time by Distance")
    ax.set_xlabel("Distance, kilometers")
    ax.set_ylabel("Delivery time, minutes")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.20), ncol=2)
    fig.tight_layout()
    plt.savefig(SCRIPT_DIR / "delivery_time_by_distance.png", bbox_inches="tight")


def plot_traffic_boxplots(data):
    plot_data = [
        data.loc[data["traffic_level"] == level, "delivery_time_minutes"].dropna()
        for level in TRAFFIC_LEVELS
    ]

    fig = plt.figure(figsize=(8, 5), dpi=300)
    ax = fig.add_subplot(111)
    box = ax.boxplot(plot_data, tick_labels=TRAFFIC_LEVELS, patch_artist=True)
    for patch, level in zip(box["boxes"], TRAFFIC_LEVELS):
        patch.set_facecolor(PALETTE[level])
        patch.set_alpha(0.75)
    ax.set_title("Delivery Time by Traffic Level")
    ax.set_xlabel("Traffic level")
    ax.set_ylabel("Delivery time, minutes")
    fig.tight_layout()
    plt.savefig(SCRIPT_DIR / "delivery_time_by_traffic_level.png", bbox_inches="tight")


def plot_busyness_weather_trends(data):
    clean_data = data.dropna(subset=["restaurant_busyness", "delivery_time_minutes"]).copy()
    bins = np.arange(0, 111, 10)
    clean_data["busyness_bin"] = pd.cut(clean_data["restaurant_busyness"], bins=bins)

    means = pd.pivot_table(
        clean_data,
        values="delivery_time_minutes",
        index="busyness_bin",
        columns="weather",
        aggfunc="mean",
        observed=True,
    ).reindex(columns=WEATHER_LEVELS)

    centers = np.array([interval.mid for interval in means.index])

    fig = plt.figure(figsize=(9, 5), dpi=300)
    ax = fig.add_subplot(111)
    for level in WEATHER_LEVELS:
        ax.plot(
            centers,
            means[level].values,
            marker="o",
            linewidth=2,
            label=level,
            color=PALETTE[level],
        )
    ax.set_title("Delivery Time by Restaurant Busyness and Weather")
    ax.set_xlabel("Restaurant busyness")
    ax.set_ylabel("Mean delivery time, minutes")
    ax.legend(title="Weather", loc="upper center", bbox_to_anchor=(0.5, 1.22), ncol=3)
    fig.tight_layout()
    plt.savefig(SCRIPT_DIR / "delivery_time_by_busyness_weather.png", bbox_inches="tight")


def main():
    configure_plots()

    data = make_dataset()
    data.to_csv(OUTPUT_PATH, index=False)

    print(f"Wrote {len(data)} rows to {OUTPUT_PATH}")
    print("\nDelivery time summary:")
    print(data["delivery_time_minutes"].describe())
    print("\nTraffic counts:")
    print(data["traffic_level"].value_counts().reindex(TRAFFIC_LEVELS))
    print("\nWeather counts:")
    print(data["weather"].value_counts().reindex(WEATHER_LEVELS))
    print("\nMissing values:")
    print(data.isna().sum())

    plot_delivery_time_distribution(data)
    plot_distance_relationship(data)
    plot_traffic_boxplots(data)
    plot_busyness_weather_trends(data)

    if "--no-show" in sys.argv:
        plt.close("all")
    else:
        plt.show()


if __name__ == "__main__":
    main()
