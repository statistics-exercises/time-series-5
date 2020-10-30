# Calculating the event that occurs first

CoIn this next two exercises we are going to look at how we can solve one of the problems that you have looked at analytically this week by writing a computer program.  The problem we are going to look at is the one about Alice and Bob and the bus stop.  If you remember this problem goes:

_Bob is waiting to catch a bus at the bus stop.  Alice, meanwhile, is in the library.  If the time Alice spends in the library is an exponentially distributed random variable with parameter 5 and the time it takes a bus to arrive is an exponentially distributed random variable with parameter 4 what is the probability that Alice meets Bob at the bus stop._

In the video we solved this problem using the conditional expectation theorem and some calculus.  This is the correct way to solve this problem but it is useful to know how the problem can be solved by running a simulation because we can get insight that we might not get otherwise.  In this first exercise we are, therefore, going to write a function to work out which event occurs first.  To complete the exercise you must:

1. Write a function called `exponential` that takes a parameter called `lam`.  This function should return an exponential random variable from a distribution with the parameter equal to `lam`.
2. Write a second function called `firstevent` that generates two exponential random variables that give the arrival time of Alice and the Bus.  Your function should return a 1 if Alice meets Bob at the bus stop and a zero otherwise. The arguments to this function `lam1` and `lam2` are the parammeters of the exponential time that give the arrival times for Alice and the Bus.
