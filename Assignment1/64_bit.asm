segment .data

msg db "The sum is:", 0xA,0xD 
len equ $ - msg   

segment .bss
   sum resb 1
   


segment .text
global main

main:
   mov     rax, 1    
   mov     rbx, 2      
   add     rax, rbx 
   add     rax, '0'
   mov 	[sum], rax
   mov	rsi,msg	
   mov	rdx, len
   mov	rdi,1	
   mov	rax,1	
   syscall
	
   mov	rsi,sum
   mov	rdx, 1
   mov	rdi,1	
   mov	rax,4	
   syscall
	
   mov	rax,1	
   syscall


   ;rax->eax rax are 64 bit registers works only with 64 bit compiler
