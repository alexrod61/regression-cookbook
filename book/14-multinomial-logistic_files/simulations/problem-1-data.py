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
SEED = 1411
N_STUDENTS = 750

LUNCH_LEVELS = ["Cafeteria", "Packed_Lunch", "Food_Delivery", "Fast_Food"]
PALETTE = {
    "Cafeteria": "#0072B2",
    "Packed_Lunch": "#009E73",
    "Food_Delivery": "#D55E00",
    "Fast_Food": "#CC79A7",
}


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def gaussian_bump(x, center, width):
    return np.exp(-0.5 * ((x - center) / width) ** 2)


def softmax(utilities):
    shifted = utilities - utilities.max(axis=1, keepdims=True)
    exp_utilities = np.exp(shifted)
    return exp_utilities / exp_utilities.sum(axis=1, keepdims=True)


def make_dataset(n_students=N_STUDENTS, seed=SEED):
    rng = np.random.default_rng(seed)

    weekly_food_budget = rng.gamma(shape=5.5, scale=12.0, size=n_students) + 12
    weekly_food_budget += rng.normal(0, 7, size=n_students)
    weekly_food_budget = np.clip(weekly_food_budget, 18, 185)

    time_between_classes = rng.normal(55, 28, size=n_students)
    tight_schedule = rng.random(n_students) < 0.25
    time_between_classes[tight_schedule] = rng.normal(18, 8, size=tight_schedule.sum())
    time_between_classes = np.clip(time_between_classes, 5, 150)

    distance_from_home = rng.lognormal(mean=1.65, sigma=0.85, size=n_students)
    distance_from_home = np.clip(distance_from_home, 0.2, 42)

    budget_z = (weekly_food_budget - weekly_food_budget.mean()) / weekly_food_budget.std()
    time_z = (time_between_classes - time_between_classes.mean()) / time_between_classes.std()
    distance_z = (np.log1p(distance_from_home) - np.log1p(distance_from_home).mean()) / np.log1p(distance_from_home).std()

    meal_plan_prob = sigmoid(
        0.9
        - 0.65 * distance_z
        - 0.20 * budget_z
        + 0.18 * np.sin(time_between_classes / 22)
        + rng.normal(0, 0.45, size=n_students)
    )
    has_meal_plan = rng.binomial(1, meal_plan_prob, size=n_students)

    restriction_prob = sigmoid(
        -1.45
        + 0.16 * distance_z
        + 0.12 * np.cos(weekly_food_budget / 19)
        + rng.normal(0, 0.25, size=n_students)
    )
    dietary_restriction = rng.binomial(1, restriction_prob, size=n_students)

    short_gap = gaussian_bump(time_between_classes, center=14, width=9)
    cafe_gap = gaussian_bump(time_between_classes, center=55, width=24)
    delivery_gap = gaussian_bump(time_between_classes, center=105, width=34)

    shared_noise = rng.normal(0, 0.18, size=(n_students, len(LUNCH_LEVELS)))

    cafeteria_utility = (
        0.55
        + 1.15 * has_meal_plan
        + 0.65 * cafe_gap
        - 0.18 * budget_z
        - 0.20 * dietary_restriction
        - 0.18 * distance_z
        + 0.12 * np.sin(distance_from_home / 4.5)
    )
    packed_utility = (
        -0.05
        - 0.70 * budget_z
        + 0.58 * dietary_restriction
        + 0.42 * distance_z
        + 0.45 * short_gap
        - 0.34 * has_meal_plan
        + 0.15 * np.cos(time_between_classes / 18)
    )
    delivery_utility = (
        -0.50
        + 0.92 * budget_z
        + 0.52 * delivery_gap
        + 0.18 * distance_z
        - 0.28 * has_meal_plan
        + 0.12 * time_z**2
        + 0.16 * budget_z * distance_z
    )
    fast_food_utility = (
        -0.22
        + 0.38 * budget_z
        + 0.72 * short_gap
        - 0.34 * dietary_restriction
        - 0.22 * has_meal_plan
        + 0.18 * np.sin(weekly_food_budget / 14)
        - 0.10 * time_z**2
    )

    utilities = np.column_stack(
        [
            cafeteria_utility,
            packed_utility,
            delivery_utility,
            fast_food_utility,
        ]
    )
    probabilities = softmax(utilities + shared_noise)

    lunch_choice = [
        rng.choice(LUNCH_LEVELS, p=row_probabilities)
        for row_probabilities in probabilities
    ]

    data = pd.DataFrame(
        {
            "weekly_food_budget": np.round(weekly_food_budget, 2),
            "time_between_classes": np.round(time_between_classes, 1),
            "distance_from_home": np.round(distance_from_home, 2),
            "has_meal_plan": np.where(has_meal_plan == 1, "Yes", "No"),
            "dietary_restriction": np.where(dietary_restriction == 1, "Yes", "No"),
            "lunch_choice": pd.Categorical(lunch_choice, categories=LUNCH_LEVELS),
        }
    )

    missing_budget = rng.random(n_students) < 0.025
    missing_time = rng.random(n_students) < 0.020
    data.loc[missing_budget, "weekly_food_budget"] = np.nan
    data.loc[missing_time, "time_between_classes"] = np.nan

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


def plot_lunch_counts(data):
    counts = data["lunch_choice"].value_counts().reindex(LUNCH_LEVELS)

    fig = plt.figure(figsize=(8, 5), dpi=300)
    ax = fig.add_subplot(111)
    ax.bar(counts.index, counts.values, color=[PALETTE[level] for level in counts.index])
    ax.set_title("Distribution of Campus Lunch Choice")
    ax.set_xlabel("Lunch choice")
    ax.set_ylabel("Number of students")
    ax.tick_params(axis="x", rotation=20)
    fig.tight_layout()
    plt.savefig("lunch_choice_counts.png", bbox_inches="tight")


def plot_budget_by_choice(data):
    plot_data = [
        data.loc[data["lunch_choice"] == level, "weekly_food_budget"].dropna()
        for level in LUNCH_LEVELS
    ]

    fig = plt.figure(figsize=(9, 5), dpi=300)
    ax = fig.add_subplot(111)
    box = ax.boxplot(plot_data, tick_labels=LUNCH_LEVELS, patch_artist=True)
    for patch, level in zip(box["boxes"], LUNCH_LEVELS):
        patch.set_facecolor(PALETTE[level])
        patch.set_alpha(0.7)
    ax.set_title("Weekly Food Budget by Lunch Choice")
    ax.set_xlabel("Lunch choice")
    ax.set_ylabel("Weekly food budget")
    ax.tick_params(axis="x", rotation=20)
    fig.tight_layout()
    plt.savefig("weekly_food_budget_by_lunch_choice.png", bbox_inches="tight")


def plot_meal_plan_proportions(data):
    props = pd.crosstab(
        data["has_meal_plan"],
        data["lunch_choice"],
        normalize="index",
    ).reindex(columns=LUNCH_LEVELS)

    fig = plt.figure(figsize=(8, 5), dpi=300)
    ax = fig.add_subplot(111)
    bottom = np.zeros(len(props.index))
    x = np.arange(len(props.index))
    for level in LUNCH_LEVELS:
        ax.bar(
            x,
            props[level].values,
            bottom=bottom,
            label=level,
            color=PALETTE[level],
        )
        bottom += props[level].values

    ax.set_xticks(x)
    ax.set_xticklabels(props.index)
    ax.set_ylim(0, 1)
    ax.set_title("Lunch Choice Proportions by Meal Plan Status")
    ax.set_xlabel("Has meal plan")
    ax.set_ylabel("Proportion")
    ax.legend(title="Lunch choice", bbox_to_anchor=(1.02, 1), loc="upper left")
    fig.tight_layout()
    plt.savefig("lunch_choice_by_meal_plan_status.png", bbox_inches="tight")


def plot_time_gap_trends(data):
    clean_data = data.dropna(subset=["time_between_classes"]).copy()
    bins = np.arange(0, 166, 15)
    clean_data["time_bin"] = pd.cut(clean_data["time_between_classes"], bins=bins)

    props = pd.crosstab(
        clean_data["time_bin"],
        clean_data["lunch_choice"],
        normalize="index",
    ).reindex(columns=LUNCH_LEVELS)

    centers = np.array([interval.mid for interval in props.index])

    fig = plt.figure(figsize=(9, 5), dpi=300)
    ax = fig.add_subplot(111)
    for level in LUNCH_LEVELS:
        ax.plot(
            centers,
            props[level].values,
            marker="o",
            linewidth=2,
            label=level,
            color=PALETTE[level],
        )

    ax.set_title("Lunch Choice Proportions by Time Between Classes")
    ax.set_xlabel("Time between classes, minutes")
    ax.set_ylabel("Proportion")
    ax.set_ylim(0, 1)
    ax.legend(title="Lunch choice", bbox_to_anchor=(1.02, 1), loc="upper left")
    fig.tight_layout()
    plt.savefig("lunch_choice_by_time_between_classes.png", bbox_inches="tight")


def main():
    configure_plots()

    data = make_dataset()
    data.to_csv(OUTPUT_PATH, index=False)

    print(f"Wrote {len(data)} rows to {OUTPUT_PATH}")
    print("\nLunch choice counts:")
    print(data["lunch_choice"].value_counts().reindex(LUNCH_LEVELS))
    print("\nMissing values:")
    print(data.isna().sum())

    plot_lunch_counts(data)
    plot_budget_by_choice(data)
    plot_meal_plan_proportions(data)
    plot_time_gap_trends(data)

    if "--no-show" in sys.argv:
        plt.close("all")
    else:
        plt.show()


if __name__ == "__main__":
    main()
