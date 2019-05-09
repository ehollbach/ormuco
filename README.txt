TECHNICAL TEST
==============

Question A
----------

For this question I have created a class Line to represent a single line segment on the x-axis.
The function do_interest accepts two lines and returns a boolean indiciating whether or not the two intersect.

Question B
----------

Here we use string comparison to achieve the objective of comparing two version strings. In order to sanitize the input we strip all trailing periods.
Several test cases for this compare_versions function are included in the main method.

Question C
----------

I chose to use memcached to solve this question. Redis would be another alternative. A decision matrix should be constructed to determine which one to use in production.

Integration is dead simple:
1. Install Python 2.7.9+ or 3.4+
2. Run `pip install pymemcache`
3. Import pymemcache.client.base and create a new base.Client

For a deployment having multiple memcached instances running on separate servers, repcached may be leveraged to have the instances replicate one another.
https://sourceforge.net/projects/repcached/files/

A service should be created that routes each incoming request to the nearest memcached instance for temporary storage, this way users of the library aren't required to locate the memcached instance on their own.
