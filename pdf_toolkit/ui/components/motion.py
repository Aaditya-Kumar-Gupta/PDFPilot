from __future__ import annotations

from PySide6.QtCore import QEasingCurve, QPoint, QParallelAnimationGroup, QPropertyAnimation, QTimer
from PySide6.QtWidgets import QGraphicsOpacityEffect, QWidget


def animate_in(widget: QWidget, *, duration: int = 240, offset: int = 18, delay: int = 0) -> QParallelAnimationGroup:
    end_pos = widget.pos()
    start_pos = QPoint(end_pos.x(), end_pos.y() + offset)
    widget.move(start_pos)

    effect = widget.graphicsEffect()
    if not isinstance(effect, QGraphicsOpacityEffect):
        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
    effect.setOpacity(0.0)

    slide = QPropertyAnimation(widget, b"pos", widget)
    slide.setDuration(duration)
    slide.setStartValue(start_pos)
    slide.setEndValue(end_pos)
    slide.setEasingCurve(QEasingCurve.Type.OutCubic)

    fade = QPropertyAnimation(effect, b"opacity", widget)
    fade.setDuration(duration)
    fade.setStartValue(0.0)
    fade.setEndValue(1.0)
    fade.setEasingCurve(QEasingCurve.Type.OutCubic)

    group = QParallelAnimationGroup(widget)
    group.addAnimation(slide)
    group.addAnimation(fade)
    widget._motion_group = group  # type: ignore[attr-defined]
    if delay:
        QTimer.singleShot(delay, group.start)
    else:
        group.start()
    return group


def animate_opacity(
    widget: QWidget,
    *,
    start: float,
    end: float,
    duration: int = 180,
) -> QPropertyAnimation:
    effect = widget.graphicsEffect()
    if not isinstance(effect, QGraphicsOpacityEffect):
        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
    effect.setOpacity(start)

    animation = QPropertyAnimation(effect, b"opacity", widget)
    animation.setDuration(duration)
    animation.setStartValue(start)
    animation.setEndValue(end)
    animation.setEasingCurve(QEasingCurve.Type.OutCubic if end > start else QEasingCurve.Type.InCubic)
    widget._opacity_animation = animation  # type: ignore[attr-defined]
    animation.start()
    return animation
