import pywasm

pywasm.log.lvl = 1

runtime = pywasm.core.Runtime()
m = runtime.instance_from_file('./target/wasm32-unknown-unknown/debug/rswasm.wasm')
r = runtime.invocate(m, 'pi', [7])
print('pi =', r[0])
