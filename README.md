# Distributed-Calculator-with-Python
 Calculator system that utilizes multiple computing resources or nodes to perform calculations. Instead of relying on a single calculator or server, the workload is distributed among multiple nodes to enhance performance, handle larger workloads, and improve fault tolerance.

 1. Client:
   - Port: No specific port, initiates connection to NetNode.
   - Description: The client is the user interface where users input the calculation requests and receive the results. It connects to the NetNode to send the calculation requests.

2. NetNode:
   - Port: 8000
   - Description: The NetNode serves as the intermediary between the client and the calculators. It receives the calculation requests from the client and forwards them to the available calculators for processing.

3. Calculator (Calculator 1 and Calculator 2):
   - Port: 9001 (Calculator 1), 9002 (Calculator 2)
   - Description: The calculators perform the actual calculations requested by the client. They receive the calculation requests from the NetNode, process them, and send the results back to the NetNode.

4. Spooler:
   - Port: 7000
   - Description: The Spooler receives the calculation results from the calculators via the NetNode. It stores the results temporarily before forwarding them to the Logger for logging.

5. Logger:
   - Port: 9000
   - Description: The Logger receives the calculation requests and results from the Spooler. It logs the requests and results to a text file for future reference or analysis.

