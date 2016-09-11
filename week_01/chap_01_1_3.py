"""
Keeping the last N items
"""

from collections import deque


def main():
    commands = ['add', 'clone', 'delete', 'commit', 'status']
    q = deque(maxlen=3)
    for item in commands:
        q.append(item)
    print(q)


main()
