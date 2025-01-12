import pickle
import numpy as np
import shap
import matplotlib.pyplot as plt



with open('SHAP/sequence_shap_values.pkl', 'rb') as f:
    shap_values = pickle.load(f)

feature_names = ['window_pos_' + str(i) for i in range(1,34)]
# make font size larger
plt.rcParams.update({'font.size': 16})

# Visualize SHAP values as a bar plot in original order
ordering = np.arange(len(feature_names))  # Preserve original order
shap.plots.bar(shap_values, max_display=len(feature_names), order=ordering)
# plt.savefig("bar_plot.pdf", format="pdf")
plt.show()
plt.close()