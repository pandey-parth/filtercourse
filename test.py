import pandas as pd
import numpy as np
import streamlit as st


def main():
    st.title('Filtering Coursera Courses')
    st.sidebar.title('Filters')
    st.markdown('Use filters to get best possible courses')


    # @st.cache(persist=True)
    # def load_data():
    df=pd.read_excel(r'C:\Users\parth\Desktop/Book1_final.xlsx')
    df.rename(columns={'Category(1 ai, 2 comps, 3 business)':'course_category'},inplace=True)


    df=df.dropna()
    ind=np.arange(len(df))
    df=df.set_index(ind)
    arr=[]
    for i in range(len(df)):
        s=df.loc[i,'course_students_enrolled']
        
        if type(s)==int:
            arr.append(k)
        
        elif s[-1]=='k':
            k=float(s[:-1])
            k=k*1000
        elif s[-1]=='m':
            k=float(s[:-1])
            k=k*1000000
        arr.append(k)
    
    df['course_students_enrolled']=arr

    arr=[]
    for i in range(len(df)):
        s=df.loc[i,'course_category']
        if type(s)==int:
            if s==1:
                arr.append('Artificial Intelligence')
            elif s==2:
                arr.append('Computing')
            elif s==3:
                arr.append('Business')
            else:
                arr.append('Other')
        else:
            if s=='?':
                arr.append('Other')
            else:
                k=int(s[0])
                if k==1:
                    arr.append('Artificial Intelligence')
                elif k==2:
                    arr.append('Computing')
                elif k==3:
                    arr.append('Business')
    

    df['course_category']=arr

    # return df

    # df=load_data()

    st.sidebar.subheader('Course Certification Type')
    course_type=st.sidebar.selectbox('Course Certification Type',('PROFESSIONAL CERTIFICATE', 'SPECIALIZATION', 'COURSE',
       'GUIDED PROJECT'))

    st.sidebar.subheader('Course Difficulty')
    diff=st.sidebar.selectbox('Difficulty',('Beginner', 'Intermediate', 'Mixed', 'Advanced'))

    df1=df[df['course_Certificate_type']==course_type]
    df2=df[df['course_difficulty']==diff]
    df3=pd.merge(df1,df2,how='inner')
    

    st.sidebar.subheader('Course Category')
    category= st.sidebar.selectbox('Category',('Artificial Intelligence','Computing','Business','Other'))
    df4=df[df['course_category']==category]
    df5=pd.merge(df3,df4,how='inner')
    

    st.subheader('Sort By')
    sort=st.selectbox('Sort',('Students Enrolled','Rating','Random'))

    if sort=='Students Enrolled':
        df6=df5.sort_values(by=['course_students_enrolled'],ascending=False)
        st.write(df6[['course_title','course_link','course_rating','course_students_enrolled']])
    elif sort=='Rating':
        df7=df5.sort_values(by=['course_rating'],ascending=False)
        st.write(df7[['course_title','course_link','course_rating','course_students_enrolled']])
    
    else: 
        st.write(df5[['course_title','course_link','course_rating','course_students_enrolled']])
    
    if st.sidebar.checkbox("Show raw data", False):
        st.subheader(" Raw Data")
        st.write(df)
if __name__ == '__main__':
    main()

