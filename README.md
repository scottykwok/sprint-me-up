# Sprint-Me-Up: PyCon HK 2025 Sprint Registration

Due to high demand for the PyCon HK 2025 Sprint, we’re thrilled to release **40 additional tickets** for developers! Tickets are allocated on a first-come, first-served basis, so register quickly. Follow the steps below to secure your spot.

## Steps

1. Fork this repository to your GitHub account.
2. Join the [Python Hong Kong User Group Discord server](https://bit.ly/pyconhk) and visit the **#2025-sprint** channel to obtain the registration token.
3. Run the `registration.py` script. Use your Ticket ID from your Day 1 Eventbrite ticket (found below the QR code, it’s a long ID).
4. Create a Pull Request to submit your ticket file: `tickets/<ticket_id>.txt`.
5. After submitting your Pull Request, verify that the Status Check is green. A red status indicates an invalid submission.
6. The organizers will review and merge your Pull Request (first-come, first-served basis). If merged, your ticket is confirmed.


## For Organizers

1. Create an environment named `check-ticket-runner` in GitHub Environments.
2. Add an environment secret named `TICKET_TOKEN` to the `check-ticket-runner` environment and input your secret value.