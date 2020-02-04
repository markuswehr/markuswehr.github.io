{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Diagonal Difference"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "https://www.hackerrank.com/challenges/diagonal-difference/problem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#\n",
    "# Complete the 'diagonalDifference' function below.\n",
    "#\n",
    "# The function is expected to return an INTEGER.\n",
    "# The function accepts 2D_INTEGER_ARRAY arr as parameter.\n",
    "#\n",
    "\n",
    "def diagonalDifference(arr):\n",
    "    # Write your code here\n",
    "    \"\"\"First flattens the matrix, then calculates right and left diagonal\"\"\"\n",
    "    flattened=[number for numbers in arr for number in numbers]\n",
    "    left=functools.reduce(lambda x,y:x+y,flattened[::n+1])\n",
    "    right=functools.reduce(lambda x,y:x+y,flattened[::n-1][1:-1])\n",
    "    \n",
    "    return abs(left-right)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
