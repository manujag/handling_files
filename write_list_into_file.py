
i=1;list_to_write=[]
while i<30000:
    a=str(i**2)+'seeqrthdfshjshagfnoerngorengvoengneognsren_'+str(i**3)+'_'+str(i**4)
    #print(a)
    list_to_write.append(a)
    i+=1
#with open('test_file.txt','w') as file:
#    file.writelines(list_to_write)

with open('test_file.txt', 'w') as f:
    for item in list_to_write:
        f.write("%s\n" % item)
