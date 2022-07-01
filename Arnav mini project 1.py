 Get The Last 'x' Rows Of The Future Data Set
x_future = df.drop(['Prediction'], axis=1)[:-f_days]
x_future = x_future.tail(f_days)
x_future = np.array(x_future)
# print(x_future)

# Show The Model Tree Prediction
tree_prediction = tree.predict(x_future)

# Show The Model Linear Regression Prediction
lr_prediction = lr.predict(x_future)
