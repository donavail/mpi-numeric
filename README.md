# MPI-Numeric
This repository contains how to execute a numeric program in python using MPI with an Ubuntu Master &amp; 3 Ubuntu Slave

# Things to be prepared:

1. Ubuntu Desktop Master
2. 3 Ubuntu Desktop Slaves
3. MPI (Master and Slaves)
4. SSH (Master and Slaves)
5. NFS (Master and Slaves)
6. Bubble Sort Coding

# Topology Flowchart
![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/5ecd1689-7c0e-47a2-9b67-309ded47b291)

# /etc/hosts File Configuration
1. Ensure that the Ubuntu Desktop installation uses Network Bridged Adapter, and that each Master and Slave is connected to the internet with known IP configurations.
2. Execute the command to modify the /etc/hosts file as shown in the image below.
![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/b1993c83-0277-4c6d-9f27-292465fff1e5)

3. Next, configure the /etc/hosts file following the instructions in the image below.
![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/ea96bb41-d543-46d0-b15a-eea0b2f9842b)

# Creating a New User
1. On Ubuntu Master and Slaves, create a new user using the following command.  
   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/3b4ff9fa-1da9-4ab3-87e3-f0c73b413480)
   
   Follow all the steps prompted by the system, making sure the username is the same on the Master and each Slave.

3. After creating a new user, log in to that account on the Master and each Slave using the following command.
![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/9fa49909-8cf5-4f78-9538-d8792219c640)

# SSH Configuration
1. Install SSH first on Ubuntu Master and Slaves with the following command.

   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/6c725a24-aa31-48a0-a149-4c4aaf53aa7e)

2. After installation, check the SSH status with the following command.

   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/27e325df-974c-4c62-8784-72ae5e422c6f)

   Ensure that the result matches the image below.
   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/70d6808f-c603-4696-9e00-a463630ac01a)


# Generate & Copy Keygen from Master to Slave
1. On Ubuntu Master, run the following command.

   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/453f9acb-1d35-4659-b490-9edb2dc778e0)

   Follow the instructions prompted by the system. Afterward, there will be a .ssh folder containing id_rsa and id_rsa.pub files.

2. Next, on Ubuntu Master, copy the contents of the id_rsa.pub file to the authorized_keys file using SSH, as shown in the image below.

   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/86af92f4-e7a7-43d3-9a88-68b91d18eeba)
   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/58123bab-965c-4942-93e1-1f02dc8b7532)

   Repeat this process from Master to each Slave by changing the host.

# NFS Configuration
1. On Ubuntu Master and Slaves, create directories with the following command.

   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/ebcc0034-e704-4b56-b2cd-72e04c3675b1)

2. Next, on Ubuntu Master, install NFS Server with the following command.

   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/49d72082-a950-442e-9697-1453599be432)

3. On Ubuntu Master, open the /etc/exports file using nano and add lines as seen in the image below.

   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/3f9c2992-30fc-4ef2-b2eb-0ed8cf314006)
   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/6be38817-3779-4510-9b62-413239fcf727)

4. After configuring the /etc/exports file, enter the following command.

   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/7067b2db-8d30-4a80-abb1-a0708f2ca946)
   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/674f6b4a-8e23-49d7-954e-506b96d240e8)

5. Then, on Ubuntu Slaves, install NFS Client with the following command.

   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/87753150-f2b3-4925-8688-80b740622d19)

6. Finally, perform mounting on all three Ubuntu Slaves using the following command.

   ![image](https://github.com/donavail/mpi-bubblesort/assets/150001914/fb3a13d3-ea11-4473-aa80-2ce6d61d030b)

# Numeric Program Execution
1. To activate the numeric program execution, begin by installing MPI on both the Ubuntu Master and Server using the following commands.

   ![image](https://github.com/donavail/mpi-numeric/assets/150001914/ff8773b4-d3d4-490d-a7a4-d126e2979522)

2. Next, on the Ubuntu Master, create a new Python file in the shared folder using the command below.

   ![image](https://github.com/donavail/mpi-numeric/assets/150001914/15aa7f25-ff6e-45fc-a188-4186d0b262a0)

   ![image](https://github.com/donavail/mpi-numeric/assets/150001914/9303ff96-5cbc-4cd6-b9f8-4237a2706350)

3. Ensure that the installation of NumPy has been completed before executing the numeric program.

   ![image](https://github.com/donavail/mpi-numeric/assets/150001914/758cdcfc-1fe1-4397-9542-bdea5a6fc0c6)

4. Before running the numeric code, perform MPI testing first with the following command.

   ![image](https://github.com/donavail/mpi-numeric/assets/150001914/7ed5fd0b-78ae-41fe-ac9f-15a26fdd8158)

5. Add the numeric code to the previously created Python file using the command below.

   ![image](https://github.com/donavail/mpi-numeric/assets/150001914/340615a5-3807-466a-b8a8-09e68bdfc769)

6. Finally, run the file using the following command to generate the following outputs:
   - Execution without MPI

     ![image](https://github.com/donavail/mpi-numeric/assets/150001914/93c0ae10-2345-42d0-9d6c-0f3f7f8054b1)

   - Execution with MPI Master Only
  
     ![image](https://github.com/donavail/mpi-numeric/assets/150001914/1afdbcb0-d435-44de-a920-d28390e7a2d2)

   - Execution with MPI Master & Slave1
  
     ![image](https://github.com/donavail/mpi-numeric/assets/150001914/cff2a884-5d68-463c-a16d-886dc0afa6e4)

   - Execution with MPI Master, Slave1, & Slave2
  
     ![image](https://github.com/donavail/mpi-numeric/assets/150001914/8a9eadfa-1555-4b46-93d9-434c4abb9392)

   - Execution with MPI Master, Slave1, Slave2, & Slave3
  
     ![image](https://github.com/donavail/mpi-numeric/assets/150001914/14780ad2-cc5f-4367-aa9b-ff0ee8cf223a)
