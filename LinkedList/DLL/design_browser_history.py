from typing import *

class Browser:
    class Node:
        def __init__(self,url):
            self.url=url
            self.next=None
            self.prev=None

    def __init__(self, homepage: str) -> None:
        # Write you code here
        self.head=self.Node(homepage)
        self.curr=self.head

    def visit(self, url: str) -> None:
        # Write you code here
        newNode=self.Node(url)
        self.curr.next=newNode
        newNode.prev=self.curr
        self.curr=newNode

    def back(self, steps: int) -> str:
        while steps:
            if self.curr.prev:
                self.curr=self.curr.prev
            else:
                break
            steps-=1
        return self.curr.url
        # Write you code here
        

    def forward(self, steps: int) -> str:
        while steps:
            if self.curr.next:
                self.curr=self.curr.next
            else:
                break 
            steps-=1
        return self.curr.url
        # Write you code here
        
