# Visualize The Data
p = tree_prediction
valid = df[X.shape[0]:]
valid['Prediction'] = p
plt.figure(figsize=(16, 8))
plt.title('Adani Greens')