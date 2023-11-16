import matplotlib.pyplot as plt

def plot_residuals(features_to_plot, test_features,test_label, prediction):
    num_features = len(features_to_plot)
    num_rows = (num_features // 3) + (1 if num_features % 3 != 0 else 0)

    fig, axes = plt.subplots(num_rows, 3, figsize=(15, num_rows * 5), sharey=True)

    for i, feature in enumerate(features_to_plot):
        row_index = i // 3
        col_index = i % 3

        residuals = test_label - prediction

        if num_rows > 1:
            ax = axes[row_index, col_index]
        else:
            ax = axes[col_index]

        ax.bar(test_features[feature], residuals, color='green', label='Residuals')
        ax.set_xlabel(feature)
        ax.set_ylabel('Difference (True - Predicted)')
        ax.axhline(0, color='black', linestyle='--', linewidth=1)
        ax.set_title(f'Residuals for {feature}')
        ax.legend()

    plt.tight_layout()
    plt.show()

def plot_model_coef(train_features_std,coefficients):
    tmp = []
    for name, value in zip(train_features_std.columns, coefficients):
        tmp.append({"name": name, "value": value})
        
    features_coef = pd.DataFrame(tmp).sort_values("value")
    features_coef.head()
    plt.subplots(figsize=(5,7))
    plt.barh(features_coef.name, features_coef.value, alpha=0.6)