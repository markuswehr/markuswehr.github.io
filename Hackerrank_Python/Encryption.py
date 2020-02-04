{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Encryption"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "https://www.hackerrank.com/challenges/encryption/problem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "import os\n",
    "import random\n",
    "import re\n",
    "import sys\n",
    "\n",
    "# Complete the encryption function below.\n",
    "def encryption(s):\n",
    "    \"\"\"Encryption of strings\"\"\"\n",
    "    L=len(s)\n",
    "    floor_L=math.floor(math.sqrt(L))\n",
    "    ceil_L=math.ceil(math.sqrt(L))\n",
    "    \n",
    "    # Find row and col, where row<=col, row*col>=L, and where min(row*col)\n",
    "    areas={(f,c): f*c for f in range(floor_L,ceil_L+1) for c in range(floor_L,ceil_L+1) if f<=c and f*c>=L}\n",
    "    min_area=min(areas, key=areas.get)\n",
    "    \n",
    "    # Find nth element in string, where n==col and row iterable\n",
    "    encrypted=[s[r::min_area[1]] for r in range(min_area[1])]\n",
    "    encrypted=' '.join(encrypted)\n",
    "    \n",
    "    return encrypted"
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
