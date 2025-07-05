import pickle
import numpy as np
import shap
import matplotlib.pyplot as plt

def bin_and_plot_custom(shap_and_distances, custom_bins, bin_labels):
    """
    Bin SHAP values by distance using custom bins and plot the results.

    Parameters:
        shap_and_distances: List of tuples (shap_values, distance_values)
        custom_bins: List of distance thresholds to define bins (e.g., [0, 5, 10, 20, 30])
        bin_labels: List of labels for the bins
    """
    all_binned_shap_values = []
    avg_counts = np.zeros(len(custom_bins) - 1)
    for shap_values, distance_values in shap_and_distances:
        # Separate the zero-distance residue and the remaining residues
        zero_distance_mask = distance_values == 0
        non_zero_mask = ~zero_distance_mask

        # Group SHAP values by distance bins
        binned_shap_values = [np.mean(shap_values[zero_distance_mask])]  # Start with the zero-distance group
        for i in range(len(custom_bins) - 1):
            # Mask to select residues in the current bin
            mask = (distance_values >= custom_bins[i]) & (distance_values < custom_bins[i + 1]) & non_zero_mask
            #print number of residues in each bin
            # print("Number of residues in bin", i, ":", np.sum(mask))
            avg_counts[i] += np.sum(mask)
            # Average SHAP values in this bin
            avg_shap_value = np.mean(shap_values[mask]) if np.any(mask) else 0
            binned_shap_values.append(avg_shap_value)

        all_binned_shap_values.append(binned_shap_values)
        

    # Average the binned SHAP values across all proteins
    mean_binned_shap_values = np.mean(all_binned_shap_values, axis=0)

    avg_counts = avg_counts / len(shap_and_distances)

    print("Average number of residues in each bin:", avg_counts)
    # Format the results as a SHAP Explanation object
    shap_explanation = shap.Explanation(
        values=mean_binned_shap_values,
        base_values=0,  # Base value can be set as needed
        feature_names=bin_labels
    )

    ordering = np.arange(len(bin_labels))

    # Plot using shap.plots.bar
    shap.plots.bar(shap_explanation, max_display=len(bin_labels), order=ordering)
    plt.title("Grouped Absolute SHAP Values (Custom Bins)")


if __name__ == "__main__":
    with open('SHAP/sequence_shap_values_DBPTM.pkl', 'rb') as f:
        shap_values = pickle.load(f)
    
    feature_names = ['embedding_pos_' + str(i) for i in range(33)]

    # Visualize SHAP values as a bar plot in original order
    ordering = np.arange(len(feature_names))  # Preserve original order
    shap.plots.bar(shap_values, max_display=len(feature_names), order=ordering)
    plt.show()
    plt.close()

    # Load SHAP values and distances
    with open('SHAP/shap_and_distances_DBPTM.pkl', 'rb') as f:
        shap_and_distances = pickle.load(f)
    # Define custom bins and labels
    custom_bins = [0, 4, 8, 12, 20, 30, np.inf]  # Example: distances in Angstroms with the last bin as "above 30"
    bin_labels = ["0 (Target)", "0-4 Å", "4-8 Å", "8-12 Å", "12-20 Å", "20-30 Å", ">30 Å"]

    # Perform binning and plotting
    bin_and_plot_custom(shap_and_distances, custom_bins, bin_labels)
