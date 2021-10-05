# 3xPlus1

In the chase of infinity, a number which can not be extrapolated by its very nature, 3xPlus1 aims to create a public database of observations of each maximum in ascending order.

## What Is 3x+1?

3x+1, or the **Collatz conjecture**, takes a number, and if it is odd, multiplies by three, else divides by two. Pretty simple, right? Staticians and mathmeticians who are passionate about the infinite are led to believe that there is a number that could be multiplied by three plus one all the way to infinity, meaning it never stops, or even simplier put, never reaches an even number. When it does reach an even number, the halving always ends in a violent spiral to an infinite loop of 4, 2, 1, 4. If you're interested in learning more about 3x+1, more information can be found [here](https://en.wikipedia.org/wiki/Collatz_conjecture).

## What Does The Program Do?

3xPlus1 does one thing currently, it stores information about each number, such as:

- The current maximum sequence length (all the numbers an iteration 'reaches' before returning to 4, 2, 1).
- Positive and negative 'polarity count' (count of positive and negative numbers, each).
- The sum of all numbers in an iterations sequence.
- The average of all numbers in an iterations sequence.
- The variance of the sequence.
- The standard deviation of the sequence.

Currently, that is all it does and all it needs to do. I am aggregating this data to further analyze it, as I believe there could be a correlation or pattern that could lead to an exponential formula to better 'estimate' the next highest number based on the data above.

## Future implementation

There is a lot of potential for add-on, so if you have any suggestions, please feel free to email me at kaharvell@gmail.com!
