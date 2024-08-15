from app_package.models import db, Status, Transition
from flask import Blueprint, jsonify, request

# Adjust the StatusListAPI.get method:
def get(self):
    statuses = Status.query.all()
    transitions = Transition.query.all()
    status_data = []

    # Determine "orphan" and "final" statuses
    status_reachable = {status.id: False for status in statuses}
    status_reachable[Status.query.filter_by(is_initial=True).first().id] = True
    status_final = {status.id: True for status in statuses}

    for transition in transitions:
        status_reachable[transition.to_status_id] = True
        status_final[transition.from_status_id] = False

    for status in statuses:
        label = []
        if status.is_initial:
            label.append("initial status")
        if not status_reachable[status.id]:
            label.append("orphan status")
        if status_final[status.id]:
            label.append("final status")
        status_data.append({"name": status.name, "label": ', '.join(label)})

    return jsonify(status_data)
