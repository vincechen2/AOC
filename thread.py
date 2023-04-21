import sys
import threading


val1,val2 = None, None
sem = threading.Semaphore()
i1,i2 = 0,0

def threadMethod(l1,res):
    global val1,val2
    global i1,i2
    while i1 < len(l1):
        sem.acquire()
        val1 = l1[i1]
        if val2:

            if val2 > val1:
                res.append(val1)
                val1 = None
                i1 += 1
            else:
                res.append(val2)
                val2 = None
                i2 += 1
        sem.release()
    sem.acquire()
    val1 = sys.maxsize
    sem.release()




def threadMethod2(l2,res):
    global val1, val2
    global i1,i2
    while i2 < len(l2):
        sem.acquire()
        val2 = l2[i2]
        if val1 :

            if val1 > val2:
                res.append(val2)
                val2 = None
                i2 += 1
            else:
                res.append(val1)
                val1 = None
                i1 += 1

        sem.release()
    sem.acquire()
    val2 = sys.maxsize
    sem.release()



def inorder(root):

    if not root:
        return
    inorder(root.left)
    global val1
    val1 = root.val
    inorder(root.right)


def threadRunner():
    # simulating in order traversal of a bst
    t1, t2 = [12, 2, 4, 5, 12, 3], [3, 134, 14, 6, 2, 152]
    t1.sort()
    t2.sort()

    res = []

    t1 = threading.Thread(target=threadMethod, args=( t1, res))
    t2 = threading.Thread(target=threadMethod2, args=( t2, res))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return res

if __name__ == '__main__':
    print(threadRunner())