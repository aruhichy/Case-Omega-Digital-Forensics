
# Case Omega – Timeline Analysis Findings

## 1. Case Information

- Case ID: OCH-2026-001
- Organization: OmegaCare Multispeciality Hospital
- Incident Date: 20 November 2026
- Server: HOSP-SRV-01
- Analysis Type: Synthetic Timeline Analysis
- Time Zone: Indian Standard Time (IST)

## 2. Timeline Overview

Six synthetic event records were processed using the Python timeline-generation script.

The records were sorted chronologically to establish the sequence of activities represented in the fictional incident.

## 3. Chronological Event Analysis

| Time (IST) | Event | Observation |
|---|---|---|
| 08:45 AM | LOGIN | A user login was recorded in the fictional scenario. |
| 08:55 AM | FILE_CREATED | A new demonstration file creation event was recorded. |
| 09:05 AM | USB_INSERTION | A removable USB device connection was represented. |
| 09:12 AM | OUTBOUND_CONNECTION | An unusual outbound connection was represented. |
| 09:20 AM | FILE_MODIFICATION | File modification activity was represented. |
| 09:30 AM | INCIDENT_REPORTED | The incident was reported to the response team. |

## 4. Key Observations

1. A login event appears first in the synthetic timeline.
2. A file creation event follows the login event.
3. A USB connection is represented at 09:05 AM.
4. An unusual outbound connection is represented at 09:12 AM.
5. File modification activity is represented at 09:20 AM.
6. The incident is reported at 09:30 AM.

## 5. Suspected Attack Sequence

The fictional scenario presents the following possible sequence:

- Initial user login.
- File creation activity.
- Removable USB device connection.
- Unusual outbound network connection.
- File modification activity.
- Incident discovery and reporting.

This sequence is a scenario-based reconstruction, not a verified attack path.

## 6. Potential Security Concerns

- Unusual outbound network activity requires further investigation.
- Removable device connections should be reviewed.
- File modification events should be correlated with file-system records.
- User authentication activity should be examined for unauthorized access.

## 7. Limitations

- All six records are synthetic.
- No real Windows Event Logs were acquired.
- No actual firewall logs were examined.
- No real USB device was investigated.
- Temporal order alone does not establish causation.
- The events do not independently prove ransomware execution.

## 8. Conclusion

The Python timeline-generation script successfully processed six synthetic event records and arranged them chronologically.

The fictional sequence highlights activities that a forensic investigator would examine during a real ransomware investigation.

Further investigation would require authentic forensic evidence, validated timestamps, system logs, and independent corroboration.

**Investigation Status:** Academic simulation completed.
