# RL for Booster Walking

For the setup you can follow the instructions provided by booster at https://github.com/BoosterRobotics/booster_gym
Or if you don't want to use conda you can do it like this:

```
mkdir rl_walk && cd rl_walk
uv init --python 3.8
uv sync
uv pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
uv pip install numpy==1.21.6
wget https://developer.nvidia.com/isaac-gym-preview-4
tar -xzvf isaac-gym-preview-4
cd isaacgym/python
uv pip install -e .
git clone https://github.com/BoosterRobotics/booster_gym.git
```
Then you can start the training witjh
```
uv run train.py --task=T1
```


If you want to use this on our lab server please dont use conda.