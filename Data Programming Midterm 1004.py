#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def length(self):
        return ((self.point1.x - self.point2.x) ** 2 + (self.point1.y - self.point2.y) ** 2) ** 0.5
    
    def slope(self):
        if self.point1.x == self.point2.x:
            return None
        return (self.point1.y - self.point2.y) / (self.point1.x - self.point2.x)

p1 = Point(3, 4)
p2 = Point()
s = Segment(p1, p2)

print(s.length())
print(s.slope())


# In[3]:


WITH TemperatureComparison AS (
    SELECT
        w1.id AS id
    FROM
        Weather w1
    JOIN
        Weather w2 ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
    WHERE
        w1.temperature > w2.temperature
)

SELECT id FROM TemperatureComparison;


# In[10]:


def tough(indent, pattern):
    if pattern == 0:
        return

    spaces = ' ' * indent
    stars = '*' * pattern

    print(spaces + stars)

    tough(indent + 1, pattern - 2)
    
print("f(0,0):")
tough(0, 0)

print("\nf(0,1):")
tough(0, 1)

print("\nf(0,2):")
tough(0, 2)

print("\nf(0,4):")
tough(0, 4)


# In[ ]:




