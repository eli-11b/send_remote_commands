# send_remote_commands
Send commands to remote server

<table>
  <tr>
    <th></th>
    <th>Tasks</th>
  </tr>
  <td>
    <img src="https://github.com/user-attachments/assets/c79e9be5-3cce-44eb-a66c-9755ef3fefaa" height="250">
  </td>
  <td>
    <h3>&#x25a2; Transfer Files</h3>
    <h3>&#x25a2; Create User</h3>
    <h3>&#x25a2; Set Firewall Rule </h3>
  </td>
</table>


### Example
```
# SEND REMOTE COMMANDS
python .\send_remote_command.py --hostip "127.0.0.1" --command 'ifconfig'
```
### Pre-Built Commands

<table>
  <tr>
    <th></th>
    <th>Tasks</th>
  </tr>
  <td>
    <img src="https://github.com/user-attachments/assets/6a865fa0-a86c-425d-a3ba-2e9aa92b8102" height="250">
  </td>
  <td>
    <h3>&#x2705;check_docker</h3>
    <h3>&#x2705;restart_docker </h3>
    <h3>&#x2705;check_ip  </h3>
    <h3>&#x2705;disk_space</h3>
    <h3>&#x2705;check_mounts </h3>
  </td>
</table>

### Example Prebuilt Commands
```
# Check IP
python .\send_remote_command.py --hostip "127.0.0.1" --command 'check_ip'
```

```
# Check Status of docker service
python .\send_remote_command.py --hostip "127.0.0.1" --command 'check_docker'
```

```
# Restart Docker Service
python .\send_remote_command.py --hostip "127.0.0.1" --command 'restart_docker'
```

```
# Check Diskspace
python .\send_remote_command.py --hostip "127.0.0.1" --command 'disk_space'
```

```
# List Mounted Drives
python .\send_remote_command.py --hostip "127.0.0.1" --command 'check_mounts'
```




### DONE! Enjoy!

# Questions?
<br>
<img src="https://github.com/user-attachments/assets/710669b1-49b7-4936-834c-c523781db754"  height="150">
