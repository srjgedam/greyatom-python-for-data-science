# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((new_record,data))
age=census
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=age.std()
race_0=census[census[:,2]==0]

race_0=census[census[:,2]==0]


# In[27]:


race_0


# In[30]:


race_1=census[census[:,2]==1]
race_1


# In[31]:


race_2=census[census[:,2]==2]
race_2


# In[32]:


race_3=census[census[:,2]==3]
race_3


# In[33]:


race_4=census[census[:,2]==4]
race_4


# In[34]:


len_0=len(race_0)
len_0


# In[35]:


len_1=len(race_1)
len_1


# In[37]:


len_2=len(race_2)
len_2


# In[38]:


len_3=len(race_3)
len_3


# In[39]:


len_4=len(race_4)
len_4


# In[43]:


minority_race=3


# In[44]:


senior_citizen=census[census[0:,0]>60]


# In[45]:


senior_citizen


# In[48]:


working_hours_sum=senior_citizen.sum(axis=0)[6]
working_hours_sum


# In[49]:


senior_citizen_len=len(senior_citizen)
senior_citizen_len


# In[52]:


avg_working_hours=working_hours_sum/senior_citizen_len
avg_working_hours


# In[53]:


high=census[census[:,1]>10]
high


# In[78]:


low=census[census[:,1]<=10]
low


# In[79]:


avg_pay_high=high[:,7].sum()/len(high)
avg_pay_high


# In[ ]:





# In[80]:


avg_pay_low=low[:,7].sum()/len(low)
avg_pay_low


 


