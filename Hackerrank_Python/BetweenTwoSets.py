{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Between two sets"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "https://www.hackerrank.com/challenges/between-two-sets/problem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#\n",
    "# Complete the 'getTotalX' function below.\n",
    "#\n",
    "# The function is expected to return an INTEGER.\n",
    "# The function accepts following parameters:\n",
    "#  1. INTEGER_ARRAY a\n",
    "#  2. INTEGER_ARRAY b\n",
    "#\n",
    "\n",
    "def getTotalX(a, b):\n",
    "    # Write your code here\n",
    "    \"\"\"Calculates values between list a and b (inclusive), \n",
    "    applies list comprehension to get non-suitable values, \n",
    "    and, finally, filters suitable values \"\"\"\n",
    "    between=list(range(max(a),min(b)+1))\n",
    "    values=[val for val in between for num1 in a for num2 in b if val%num1!=0 or num2%val!=0]\n",
    "    number=len(list(filter(lambda x: x not in values, between)))\n",
    "        \n",
    "    return number"
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
