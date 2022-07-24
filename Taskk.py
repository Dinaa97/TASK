import numpy as np
import pandas as pd
import os


#function for reading the IMU recordings and labels
def IMU_Read(new_path):  

        #changing the directory to the path of the selected subject
        os.chdir(new_path) 
        List = os.listdir(new_path)

        #Removing the unnecessary hiddden files from the list
        while True:      
            if '._' in List[0]:
                List.remove(List[0])
            else:
                break
        
        #Reading the first recording from the list into a numpy array
        IMU_recordings = pd.read_csv(List[0],header = None).values 
        IMU_recordings = IMU_recordings[1:,1:]    #Removing the header and the time column
        IMU_recordings = IMU_recordings.astype(float)
    
        #Reading the first label from the list into a numpy array
        IMU_labels = pd.read_csv(List[1],header = None).values 
        IMU_labels = IMU_labels[1:,:]
        IMU_labels = IMU_labels.astype(float)

    
        #Looping on the list to append the rest of the recordings and labels
        for i in range (2,len(List)):  

            if 'labels' in List[i]:
                IMU_labels1 = pd.read_csv(List[i],header = None).values
                IMU_labels1 = IMU_labels1[1:,:]
                IMU_labels1 = IMU_labels1.astype(float)
                IMU_labels = np.append(IMU_labels,IMU_labels1,0)
                
                
            else:
                IMU_recordings1 = pd.read_csv(List[i],header = None).values
                IMU_recordings1 = IMU_recordings1[1:,1:]
                IMU_recordings1 = IMU_recordings1.astype(float)
                IMU_recordings = np.append(IMU_recordings,IMU_recordings1,0)

        return IMU_recordings, IMU_labels


#function for reading the MoCap recordings and labels
def MoCap_Read(subject_path):  

        #changing the directory to the path of the selected subject
        os.chdir(subject_path)  
        List1 = os.listdir(subject_path)

        #Removing the unnecessary hiddden files from the list
        while True:   
            if '._' in List1[0]:
                List1.remove(List1[0])     
            else:
                break
        
        #Reading the first label from the list into a numpy array
        MoCap_labels = pd.read_csv(List1[0],header = None).values  
        MoCap_labels = MoCap_labels[1:,:]           #Removing the header
        MoCap_labels = MoCap_labels.astype(float)
      
        #Reading the first recording from the list into a numpy array
        MoCap_recordings = pd.read_csv(List1[1],header = None).values 
        MoCap_recordings = MoCap_recordings[1:,:]
        MoCap_recordings = MoCap_recordings.astype(float)

        
        #Looping on the list to append the rest of the recordings and labels
        for i in range (2,len(List1)):  

            if 'labels' in List1[i]:
                MoCap_labels1 = pd.read_csv(List1[i],header = None).values
                MoCap_labels1 = MoCap_labels1[1:,:]
                MoCap_labels1 = MoCap_labels1.astype(float)
                MoCap_labels = np.append(MoCap_labels,MoCap_labels1,0)

            if 'data' in List1[i]:
                MoCap_recordings1 = pd.read_csv(List1[i],header = None).values
                MoCap_recordings1 = MoCap_recordings1[1:,:]
                MoCap_recordings1 = MoCap_recordings1.astype(float)
                MoCap_recordings = np.append(MoCap_recordings,MoCap_recordings1,0)

        return MoCap_recordings, MoCap_labels


#function returning a list containing the readings
def Recordings(subject, IMU_Path, MoCap_Path): 

    #subject number check to assure correct path
    if subject < 10 :   
        subject = '0' + str(subject)
    
    #checking if the subject is present or not
    if (os.path.isdir(IMU_Path + '/S'+str(subject)) and os.path.isdir(MoCap_Path + '/S'+str(subject))): 
        new_path = IMU_Path + '/S'+str(subject)
        subject_path = MoCap_Path + '/S'+str(subject)
        IMU_recordings, IMU_labels = IMU_Read(new_path)
        MoCap_recordings, MoCap_labels = MoCap_Read(subject_path)
        
        return [IMU_recordings, IMU_labels, MoCap_recordings, MoCap_labels] 


    if (os.path.isdir(IMU_Path + '/S'+str(subject)) and not (os.path.isdir(MoCap_Path + '/S'+str(subject)))):

         new_path = IMU_Path + '/S'+str(subject)
         IMU_recordings, IMU_labels = IMU_Read(new_path)
         print('Subject not found in OMocap Data')

         return [IMU_recordings, IMU_labels]

    if ((os.path.isdir(MoCap_Path + '/S'+str(subject))) and not os.path.isdir(IMU_Path + '/S'+str(subject))):

        subject_path = MoCap_Path + '/S'+str(subject)
        MoCap_recordings, MoCap_labels = MoCap_Read(subject_path)
        print('Subject not found in IMU Data')

        return [MoCap_recordings, MoCap_labels]

        
    else:
        print('Subject not found in either IMU Data nor MoCap Data')

        return []




def main():
    IMU_Path ='C:/Users/Dinaa/Downloads/IMU data/IMU data'
    MoCap_Path ='C:/Users/Dinaa/Downloads/OMoCap data/OMoCap data'

    x = Recordings(subject= 8,IMU_Path= IMU_Path ,MoCap_Path = MoCap_Path)
    print('Done')
    print(len(x))
    

if __name__ == "__main__":
    main()  