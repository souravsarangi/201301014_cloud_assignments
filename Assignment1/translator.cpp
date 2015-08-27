#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
   FILE * fp;

   fp = fopen ("32_bit.asm", "r+");
   char str[4],c;
   str[0]=str[1]=str[2]=str[3]=0;
   int p=0;
   while(1)
   {
      c = fgetc(fp);
      if( feof(fp) )
      { 
         break ;
      }
      if(p==1&&c=='4')
      {c='1';
         p=2;
     }
      if(p==1&&c=='\n')
      	p=0;

      str[0]=str[1];
      str[1]=str[2];
      str[2]=c;
      if(strcmp(str,"eax")==0)
      {
         str[0]='r';
         if(p==0)
        	 p=1;
      }
      if(strcmp(str,"ebx")==0)
      {
         str[0]='r';
         str[1]='d';
         str[2]='i';
      }
      if(strcmp(str,"ecx")==0)
      {
         str[0]='r';
         str[1]='s';
         str[2]='i';
      }
      if(strcmp(str,"edx")==0)
      {
         str[0]='r';
         str[1]='d';
         str[2]='x';
      }
       
      if(strcmp(str,"int")==0)
      {
      	printf("syscall\n");
      	while(fgetc(fp)!='\n');
      	str[0]=str[1]=str[2]=0;
      	c=0;
      }
       
       if( feof(fp) )
      { 
         break ;
      }

      printf("%c", str[0]);
   }
   fclose(fp);
   
   
   return(0);
}