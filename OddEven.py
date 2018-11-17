{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def oddeven(answers):\n",
    "    for answer in answers: \n",
    "        start= 0\n",
    "        for i in range (1,answer+1):\n",
    "            start=start+ i\n",
    "        if start%2==1:\n",
    "            print(\"odd\")\n",
    "        else:\n",
    "            print(\"even\")\n",
    "        print(start)\n",
    "answers=[3,10,13]\n",
    "oddeven(answers)"
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
