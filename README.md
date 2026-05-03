# AntiFallDamage

Automatically prevents fall damage for **all players** in configurable dimensions.

## Why?

Minecraft Bedrock Edition's `fallDamage` game rule is server-wide and cannot be scoped to specific dimensions. **AntiFallDamage** lets you choose exactly which dimensions have fall damage disabled, making it ideal for:

- Parkour or adventure maps in a specific dimension
- Creative or building servers
- Servers that want fall damage in the Nether/End but not the Overworld (or any combination)

## Features

- **Always-on for all players** — no commands or toggles needed
- **Dimension whitelist** — independently enable/disable protection per dimension (Overworld, Nether, The End)
- **Zero overhead** — purely event-driven, no scheduled tasks or stored state

## Configuration

Located at `plugins/AntiFallDamage/config.yml` after first run:

```yaml
# Dimensions where fall damage is disabled for ALL players.
# Remove a dimension from this list to allow fall damage there.
# Valid values: overworld, nether, the_end
dimensions:
    - overworld
    - nether
    - the_end
```

**Examples:**

- Protect only the Overworld — remove `nether` and `the_end` from the list
- Protect nowhere — set `dimensions: []`

No additional dependencies are required.

## License

[MIT](LICENSE)
