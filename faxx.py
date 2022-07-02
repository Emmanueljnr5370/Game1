#print("Hello there i'm Emmanuel Tom\nI love Programming so much")

#d = {'k1':[10,4,{'k2':['this is tricky',{'tough':[1,2,['Hello']]}]}]}

#print (d['k1'][2]['k2'][1]['tough'][2][0])
d = {'k1':[{'nest_key':['this is deep',['heluo']]}]}
print (d['k1'][0]['nest_key'][1][0][:-3])