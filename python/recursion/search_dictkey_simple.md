for the code in file : search_dictkey_simple.py, reading : 

<details>
  <summary>
    simple_dict.json
  </summary>

```json
{
  "cpu_isolation_numa_1": "-1",
  "network_config": {
    "lan1": {
      "type":"vlan",
      "vlan_id":101,
      "addresses": {
        "ip": "10.10.10.1",
        "sm": "24",
        "properties": {
          "private_vlan": true
        }
      }
    },
    "lan2": {
      "type":"vlan",
      "vlan_id":102,
      "addresses": {
        "ip": "10.10.10.1",
        "sm": "24",
        "properties": {
          "private_vlan": true
        }
      }
    }
  }
}
```
</details>

♦ if i am searching for the key : "private_vlan"
  the resault:                                                                               
  ->network_config->lan1->addresses->properties->private_vlan    
  ->network_config->lan2->addresses->properties->private_vlan

