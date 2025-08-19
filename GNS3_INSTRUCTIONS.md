# GNS3 Instructions for Juniper OSPF Lab

This document provides step-by-step instructions on how to use the generated Juniper configuration files to set up an OSPF lab in GNS3.

## 1. Create a New GNS3 Project

1.  Open GNS3 and click on **File > New blank project**.
2.  Give your project a name (e.g., `Juniper_OSPF_Lab`) and click **OK**.

## 2. Add Juniper vMX Routers to the Topology

1.  In the **Routers** section of the **Devices Toolbar**, select a Juniper vMX router (or equivalent Juniper appliance).
2.  Drag and drop two vMX routers into the project workspace. GNS3 will automatically name them `R1` and `R2` (or similar).

## 3. Connect the Routers

1.  Click on the **Add a link** button in the toolbar.
2.  Click on `R1` and select an appropriate GigabitEthernet interface (e.g., `ge-0/0/0`).
3.  Click on `R2` and select an appropriate GigabitEthernet interface (e.g., `ge-0/0/0`).

## 4. Import the Generated Configuration Files

1.  Right-click on `R1` and select **Configure** (or similar option to access the router's settings).
2.  Navigate to the **HDD** or **Config** tab (this might vary based on the appliance).
3.  Import the `gns3_configs/R1_juniper_config.txt` file. You might need to copy the content and paste it into the router's initial configuration or use a specific import function if available.
4.  Repeat the same process for `R2`, importing the `gns3_configs/R2_juniper_config.txt` file.

    **Note:** For Juniper vMX, you typically paste the configuration into the CLI after the router boots up, or you can use the `load override terminal` command in configuration mode.

## 5. Start the Routers

1.  Click on the **Start/Resume all devices** button in the toolbar.

## 6. Open a Console to the Routers

1.  Right-click on `R1` and select **Console**.
2.  Right-click on `R2` and select **Console**.

## 7. Verify the OSPF Configuration

1.  In the console of `R1`, enter configuration mode (`edit`) and then commit the configuration (`commit and-quit`).
2.  Run the following command to check the OSPF neighbors:
    ```
    show ospf neighbor
    ```
    You should see `R2` in the output.

3.  In the console of `R2`, enter configuration mode (`edit`) and then commit the configuration (`commit and-quit`).
4.  Run the same command to check the OSPF neighbors:
    ```
    show ospf neighbor
    ```
    You should see `R1` in the output.

## 8. Use Wireshark to Capture and Analyze OSPF Packets

1.  Right-click on the link between `R1` and `R2` and select **Start capture**.
2.  Wireshark will open and start capturing packets on the link.
3.  You can filter for OSPF packets by typing `ospf` in the filter bar.
4.  You can now analyze the OSPF packets, such as Hello packets, Database Description (DBD) packets, and Link-State Update (LSU) packets.