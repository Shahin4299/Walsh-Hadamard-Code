# Walsh-Hadamard-Code
Walsh Codes are a set of orthogonal codes used for multiple access channeling methods and data signal modulation particularly in international CDMA standards. 
Walsh Code is a linear code that maps n length messages to codes of length 2^n. These codes are mutually orthogonal.
These codes correspond to lines of a special square matrix called the Hadamard matrix. For a set of Walsh codes of length N, it consists of n lines to form a square matrix of n × n Walsh code.
A Hadamard matrix H of order n is an n × n matrix of 1s and -1s in which H*H^T= nI_n (In is the n × n identity matrix.) For Walsh codes, we use an Hadamard matrix of the order 2^N.
H_n=(  (H      H) 
       (H     -H) )
Walsh codes can be generated from Hadamard matrices of orders which are a power of 2. 
The rows of the matrix of order 2^N  constitutes the Walsh codes which encodes N bit sequences. 
Instead of 1 and -1 consider 1 and 0. That is consider the matrix and the codes over the field F2 or modulo 2.
