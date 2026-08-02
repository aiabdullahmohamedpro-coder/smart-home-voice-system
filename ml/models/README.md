# Saved models

| File | Task |
| ---- | ---- |
| `speaker.pkl` | `SPEAKER_TASK` |
| `command.pkl` | `COMMAND_TASK` |

```bash
python train_speaker.py --tune
python train_command.py --tune
```

```python
from src.application import SmartHomePipeline
pipe = SmartHomePipeline.create_default()
```
