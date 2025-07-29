# python-mini-projects

A collection of small, useful Python projects and scripts for everyday automation, fun, and learning.

---

## Projects

### 1. Secret Santa

A Python script for organizing a Secret Santa gift exchange. This project allows you to randomly assign each participant a person to whom they will give a gift, ensuring that:
- No one is assigned to themselves
- No one is assigned to their own partner (if couples are included)
- Each assignment is unique
- Supports both couples and single participants

#### 1.1 Features
- Simple class-based implementation
- Customizable participants (couples and singles)
- Handles assignment edge-cases to avoid unsolvable scenarios
- Optionally sends email notifications to participants (disabled by default)
- Easy to adapt for any group

#### How to Use

1. **Clone this repository**  
```python
git clone https://github.com/yourusername/python-mini-projects.git
cd python-mini-projects
```

2. **Configure your participants**  
Edit the `secret-santa-assigner.py` script:
    - Adjust `list_couples` and `list_singles` for your group
    - Fill in the `mails` dictionary if you want to use email notifications
      
3. **Run the script**

    `python secret-santa-assigner.py`

5. **(Optional) Enable emails**  
    - Fill in your actual SMTP username/password in the script
    - Emails will be sent to each participant with their assignment

#### Example configuration inside the script:

list_couples = [('ParticipantA1', 'ParticipantA2'), ...]
list_singles = ['Single1', 'Single2']
mails = {
'ParticipantA1': 'participanta1@example.com',
...
}

---

## Contributing

Want to add your own mini-project or improvement? Feel free! Open a Pull Request or create an Issue.

---

## License

This repository is open source and distributed under the MIT License.

---