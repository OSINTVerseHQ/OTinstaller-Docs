# Results and resume

## Results

Results are saved to `./results/<tool>/<target>/` using the filename pattern `<YYYYmmdd-HHMMSS>_<tool>_<target>_<runid>.<ext>` plus a `.meta.json` sidecar. Results go to `./results/` in the folder where the command is run, so run it from the same folder each time, or set `OTINSTALLER_RESULTS_DIR` to a fixed path.

Tools that ask for input, such as GHunt's login, setup wizards and menus, run on a pseudo-terminal when you are at one, so their prompts show up and the session is still saved. Values given to credential flags such as `--cookie`, `--token` or `--password` are written to `.meta.json` as `***`.

```
results/sherlock/testuser/20260929-123456_sherlock_testuser_abc123.txt
results/sherlock/testuser/20260929-123456_sherlock_testuser_abc123.meta.json
```

Results can contain personal data. Store and share them accordingly.

## Resume

If a run or install is cut off by a crash, a kill or a power loss, otinstaller leaves a job marker in `~/.otinstaller/jobs/`. Run `otinstaller resume` to handle it:

- For installs: cleans up partial state and retries the install.
- For runs: reports the interrupted run and prints the command to rerun.

Pressing Ctrl+C stops cleanly and removes the marker, so there is nothing to resume. Use `otinstaller resume --dry-run` to preview, and `--json` for machine-readable output. Partial output from interrupted runs is always kept.

_This page mirrors the [OTinstaller README](https://github.com/OSINTVerseHQ/OTinstaller)._
