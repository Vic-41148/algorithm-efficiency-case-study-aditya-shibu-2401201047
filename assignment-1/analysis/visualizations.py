"""
Visualization Utilities for Algorithm Performance Analysis

This module provides functions for creating graphical representations
of algorithm performance metrics using matplotlib.
"""

import matplotlib.pyplot as plt
import pandas as pd
import os


def ensure_output_dir():
    """Ensure the graphs output directory exists."""
    os.makedirs("graphs", exist_ok=True)


def plot_sorting_time_comparison(df):
    """
    Plot execution time comparison for sorting algorithms (log scale).

    Args:
        df: DataFrame with columns 'Algorithm', 'Input Size', 'Input Type',
            'Execution Time (s)'
    """
    ensure_output_dir()
    input_types = df["Input Type"].unique()

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Sorting Algorithm Execution Time vs Input Size (Log Scale)", fontsize=14)

    for idx, input_type in enumerate(input_types):
        ax = axes[idx]
        subset = df[df["Input Type"] == input_type]

        for algo in subset["Algorithm"].unique():
            algo_data = subset[subset["Algorithm"] == algo]
            ax.plot(
                algo_data["Input Size"],
                algo_data["Execution Time (s)"],
                marker="o",
                label=algo,
            )

        ax.set_xlabel("Input Size (n)")
        ax.set_ylabel("Execution Time (seconds)")
        ax.set_title(f"Input: {input_type.capitalize()}")
        ax.set_yscale("log")
        ax.legend()
        ax.grid(True, which="both", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig("graphs/sorting_time_comparison.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: graphs/sorting_time_comparison.png")


def plot_sorting_memory_comparison(df):
    """
    Plot memory usage comparison for sorting algorithms (log scale).

    Args:
        df: DataFrame with columns 'Algorithm', 'Input Size', 'Input Type',
            'Memory Usage (KB)'
    """
    ensure_output_dir()
    input_types = df["Input Type"].unique()

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Sorting Algorithm Memory Usage vs Input Size (Log Scale)", fontsize=14)

    for idx, input_type in enumerate(input_types):
        ax = axes[idx]
        subset = df[df["Input Type"] == input_type]

        for algo in subset["Algorithm"].unique():
            algo_data = subset[subset["Algorithm"] == algo]
            ax.plot(
                algo_data["Input Size"],
                algo_data["Memory Usage (KB)"],
                marker="s",
                label=algo,
            )

        ax.set_xlabel("Input Size (n)")
        ax.set_ylabel("Peak Memory (KB)")
        ax.set_title(f"Input: {input_type.capitalize()}")
        ax.set_yscale("log")
        ax.legend()
        ax.grid(True, which="both", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig("graphs/sorting_memory_comparison.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: graphs/sorting_memory_comparison.png")


def plot_sorting_comparisons(df):
    """
    Plot comparison count for sorting algorithms (log scale).

    Args:
        df: DataFrame with columns 'Algorithm', 'Input Size', 'Input Type',
            'Comparisons'
    """
    ensure_output_dir()
    input_types = df["Input Type"].unique()

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Sorting Algorithm Comparisons vs Input Size (Log Scale)", fontsize=14)

    for idx, input_type in enumerate(input_types):
        ax = axes[idx]
        subset = df[df["Input Type"] == input_type]

        for algo in subset["Algorithm"].unique():
            algo_data = subset[subset["Algorithm"] == algo]
            ax.plot(
                algo_data["Input Size"],
                algo_data["Comparisons"],
                marker="^",
                label=algo,
            )

        ax.set_xlabel("Input Size (n)")
        ax.set_ylabel("Number of Comparisons")
        ax.set_title(f"Input: {input_type.capitalize()}")
        ax.set_yscale("log")
        ax.legend()
        ax.grid(True, which="both", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig("graphs/sorting_comparisons.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: graphs/sorting_comparisons.png")


def plot_fibonacci_time_comparison(df):
    """
    Plot execution time comparison for Fibonacci algorithms.

    Args:
        df: DataFrame with columns 'Algorithm', 'n', 'Execution Time (s)'
    """
    ensure_output_dir()

    plt.figure(figsize=(10, 6))

    for algo in df["Algorithm"].unique():
        algo_data = df[df["Algorithm"] == algo].dropna()
        plt.plot(
            algo_data["n"],
            algo_data["Execution Time (s)"],
            marker="o",
            label=algo,
        )

    plt.xlabel("n (Fibonacci Index)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Fibonacci Algorithm Execution Time vs n")
    plt.legend()
    plt.grid(True)
    plt.savefig("graphs/fibonacci_time_comparison.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: graphs/fibonacci_time_comparison.png")


def plot_fibonacci_memory_comparison(df):
    """
    Plot memory usage comparison for Fibonacci algorithms.

    Args:
        df: DataFrame with columns 'Algorithm', 'n', 'Memory Usage (KB)'
    """
    ensure_output_dir()

    plt.figure(figsize=(10, 6))

    for algo in df["Algorithm"].unique():
        algo_data = df[df["Algorithm"] == algo].dropna()
        plt.plot(
            algo_data["n"],
            algo_data["Memory Usage (KB)"],
            marker="s",
            label=algo,
        )

    plt.xlabel("n (Fibonacci Index)")
    plt.ylabel("Peak Memory (KB)")
    plt.title("Fibonacci Algorithm Memory Usage vs n")
    plt.legend()
    plt.grid(True)
    plt.savefig("graphs/fibonacci_memory_comparison.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved: graphs/fibonacci_memory_comparison.png")


def generate_all_plots(sorting_df, fibonacci_df):
    """
    Generate all performance comparison plots.

    Args:
        sorting_df: DataFrame with sorting algorithm performance data
        fibonacci_df: DataFrame with Fibonacci algorithm performance data
    """
    print("Generating sorting algorithm plots...")
    plot_sorting_time_comparison(sorting_df)
    plot_sorting_memory_comparison(sorting_df)
    plot_sorting_comparisons(sorting_df)

    print("Generating Fibonacci algorithm plots...")
    plot_fibonacci_time_comparison(fibonacci_df)
    plot_fibonacci_memory_comparison(fibonacci_df)

    print("\nAll plots saved to graphs/ directory")
