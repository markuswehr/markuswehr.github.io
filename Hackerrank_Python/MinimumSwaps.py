{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Minimum Swaps"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "import os\n",
    "import random\n",
    "import re\n",
    "import sys\n",
    "\n",
    "# Complete the minimumSwaps function below.\n",
    "def minimumSwaps(arr):\n",
    "    \"\"\"find minimum number of swaps needed to sort list in ascending order\"\"\"\n",
    "    index=list(range(1,len(arr)+1))\n",
    "    ai_dic={index[i]: arr[i] for i in range(len(arr))}\n",
    "    diff=[0 if a-i==0 else 1 for a,i in ai_dic.items()]\n",
    "    min_swap=sum(diff)-1\n",
    "\n",
    "    return min_swap"
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
