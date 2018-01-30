'''run wrangle first'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
x = df['Revenue per Invest.'] #pick variable
x.describe()

'''select percentiles'''
median = x.median()
q25 = x.quantile(.25)
q75 = x.quantile(.75)
'''Set style'''
import matplotlib.style as style
style.available
style.use('seaborn-colorblind')

'''create chart'''
sns.set_context('poster',1.2)
ax = sns.kdeplot(x,shade=True, bw='silverman', kernel='biw', color='#9788B1')
#ax = sns.distplot(x, hist=False, norm_hist=True, rug=False, kde_kws={'bw':'silverman',"shade":"True", "kernel":'biw', "color":'#BB5761'})
ax.set_xlim((x.min() - .1) , (x.max()))
ax.set_ylim(0,10)

'''format ticks'''
y_vals = ax.get_yticks()
#ax.set_yticklabels(['{:3.1f}%'.format(x*100) for x in y_vals])
ax.axes.yaxis.set_ticklabels([])
x_vals = ax.get_xticks()
ax.set_xticklabels(['{:3.1f}%'.format(x*100)for x in x_vals])

#ax.set_xticks(np.arange(6,17))

'''format lines'''
line_len = [0,6]
line_style = 'dashed'

lines = 'y'

if lines == 'y':
    ax.vlines(median, line_len[0], line_len[1], linestyles=line_style,colors='#D8593E') #create verticle lines
    ax.text((median-.02), (line_len[1]+.09), 'Median')
    
    ax.vlines(q25, line_len[0], line_len[1], linestyles=line_style, colors='#708413')
    ax.text((q25-.01),(line_len[1]+.09), 'Q25')
    
    #ax.vlines(q75, line_len[0], line_len[1], linestyles=line_style, colors='#708413')
    #ax.text((q75-.01), (line_len[1]+.09), 'Q75')
    