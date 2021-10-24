=========
Inventory
=========

Our inventory is found at `files/ansible/inventory.yaml`, please update to reflect your own environment

.. code-block:: yaml

      ---
      all:
         children:
            firewalls:
               hosts:
                  galveston:
                     ansible_host: 192.168.105.137
                  sanantonio:
                     ansible_host: 192.168.105.146

There is a top level group called `all`, which we will be calling in our playbook.

We create our own group called `firewalls`, and embed the hosts `sanantonio` and `galveston` within it.

Each host has a unique IP address, so we declare that at the host level with `ansible_host` key.