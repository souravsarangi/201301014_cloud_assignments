segment .data

msg db "The sum is:", 0xA,0xD 
len equ $ - msg   

segment .bss
   sum resb 1
   


segment .text
global main

main:
   mov    eax, 1    
   mov    ebx, 2      
   add    eax, ebx 
   add    eax, '0'
   mov 	[sum], eax
   mov	ecx, msg	
   mov	edx, len
   mov	ebx, 1	
   mov	eax, 4	
   int   80h
	
   mov	ecx, sum
   mov	edx, 1
   mov	ebx, 1	
   mov	eax, 4	
   int   80h
	
   mov	eax, 1	
   mov   ebx, 0
   int   80h

   ;32 bit assembly compiles with both 32 bit and 64 bit compiler