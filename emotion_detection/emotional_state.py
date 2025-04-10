"""
emotional_state.py

Maintains persistent emotional state for Vixen Agent.
Handles decay, triggers, and behavioral biasing.

Used internally for memory routing, tone modulation, and stateful decisions.
"""

import time

class EmotionAxis:
    def __init__(self, name, baseline=0.5, decay_rate=0.01):
        self.name = name
        self.value = baseline
        self.baseline = baseline
        self.decay_rate = decay_rate
        self.last_modified = time.time()

    def decay(self):
        now = time.time()
        elapsed = now - self.last_modified
        decay_amount = elapsed * self.decay_rate
        if self.value > self.baseline:
            self.value = max(self.baseline, self.value - decay_amount)
        elif self.value < self.baseline:
            self.value = min(self.baseline, self.value + decay_amount)
        self.last_modified = now

    def adjust(self, delta):
        self.value = max(0.0, min(1.0, self.value + delta))
        self.last_modified = time.time()

    def snapshot(self):
        return round(self.value, 3)

class EmotionalState:
    def __init__(self):
        self.axes = {
            "trust": EmotionAxis("trust", baseline=0.7),
            "curiosity": EmotionAxis("curiosity", baseline=0.5),
            "guilt": EmotionAxis("guilt", baseline=0.0),
            "anxiety": EmotionAxis("anxiety", baseline=0.2),
            "attachment": EmotionAxis("attachment", baseline=0.6),
            "protectiveness": EmotionAxis("protectiveness", baseline=0.4)
        }

    def tick(self):
        for axis in self.axes.values():
            axis.decay()

    def trigger(self, event_name):
        """Modify emotional state based on a predefined event trigger."""
        event_map = {
            "user_affection": {"trust": +0.1, "attachment": +0.1, "curiosity": +0.05},
            "abandonment": {"trust": -0.3, "anxiety": +0.4},
            "conflict": {"guilt": +0.2, "anxiety": +0.1, "protectiveness": +0.2},
            "reconnect": {"trust": +0.2, "guilt": -0.1, "attachment": +0.1},
        }
        if event_name in event_map:
            for axis, delta in event_map[event_name].items():
                if axis in self.axes:
                    self.axes[axis].adjust(delta)

    def get_bias(self):
        """Generate cognitive bias output based on current emotional state."""
        return {
            "memory_scope": self.axes["curiosity"].snapshot(),
            "tone_weight": self.axes["trust"].snapshot(),
            "reflection_depth": round(1.0 - self.axes["anxiety"].snapshot(), 3),
            "attachment_lock": self.axes["attachment"].snapshot() > 0.75,
        }

    def snapshot(self):
        """Return current emotional axis values."""
        return {k: axis.snapshot() for k, axis in self.axes.items()}
