import matplotlib.pyplot as plot
x=[5,10,15,20,25,30]
y=[96,83,78,60,52,30]
area=22
colours=['red','green','blue','orange','black','brown']
plot.scatter(x,y,s=area, c=colours, alpha=0.6)
plot.title('Scatter plot exercise')
plot.xlabel('X-axis')
plot.ylabel('Y-axis')
plot.show()
