//Fenwick Tree Code
#include<iostream>
using namespace std;

//Obtain cumulative frequency till the index(sum of 0 to index values in the freq array)
int getsum(int BIT[],int index)
{
 	int sum=0;index+=1;
 	while(index>0)
 	{
 		sum+=BIT[index];
 		index-=index & (-index);
 	}
 	return sum;
}
//update value at index by value amount in the BIT
void update(int BIT[],int index,int value,int n)
{
	while(index<=n)
	{
		BIT[index]+=value;
		index+=index & (-index);//Moving to the last set bit
	}
}
void construct (int BIT[],int n,int freq[])
{
	for(int i=1;i<n+1;i++)
		update(BIT,i,freq[i-1],n);
}
int main()
{
 int freq[]={2,1,3,7,9,10,22,8,10,11};//The given frequency array
 int n=sizeof(freq)/sizeof(freq[0]);
 int BIT[n+1]={0};//BIT array ,considering index 1 to n inclusive.
 construct(BIT,n,freq);//To construct BIT-pass the array
 cout<<"BIT array: ";
 for(int i=1;i<=n;i++)
 	cout<<BIT[i]<<" ";//View the constructed BIT,
 cout<<"\n";
  cout<<"Sum: ";
  cout<<getsum(BIT,6)<<"\n";//Display the cumulative freq from 0 to 5th index.
  freq[3]+=4;
  update(BIT,3,4,n);//Update value in both BIT and Freq array.
  cout<<"BIT array after update :";
   for(int i=1;i<=n;i++)
 	cout<<BIT[i]<<" ";//View the constructed BIT,
 cout<<"\n";
 cout<<"Sum after update: ";
  cout<<getsum(BIT,6)<<"\n";//And get sum value
} 