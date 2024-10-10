"""
when doing multiple tasks at the same time is called multitasking both MP and MT are
used to achieve multitasking.
multi threads(thread 1 and 2)  live within a process with its own virtual memory or address space,they share this address space

While multiprocessing(process 1 and 2) they have their own address space, for communication of process 1 and 2 they use
intercommunication technique such file of a disk, or a shared memory or a message pipe

so the main difference between MT VS PT is that threads are lightweight while process are heavyweight

the benefit of MP is that error or memory leak in one process won't hurt execution of another process

but in MT if there is an error or memory leak in one thread it will hurt execution of another thread because
MT threads run in the same process

"""