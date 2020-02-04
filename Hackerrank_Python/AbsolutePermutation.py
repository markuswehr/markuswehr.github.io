{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Absolute Permutation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "https://www.hackerrank.com/challenges/absolute-permutation/problem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "import os\n",
    "import random\n",
    "import re\n",
    "import sys\n",
    "\n",
    "# Complete the absolutePermutation function below.\n",
    "def absolutePermutation(n, k):\n",
    "    \"\"\"Returns permutated list based on positional list 1 to n and absolute difference k\"\"\"\n",
    "    position=list(range(1,n+1))\n",
    "    if k==0:\n",
    "        permutation=position\n",
    "    elif len(position)%k==0:\n",
    "        k_list=k*[k]+k*[-k]\n",
    "        k_list=k_list*int(len(position)/len(k_list))\n",
    "        permutation=list(map(lambda p,k: abs(p+k),position,k_list))\n",
    "    else:\n",
    "        permutation=[-1]\n",
    "\n",
    "    return permutation"
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
