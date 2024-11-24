function solo_dimensionwalker
 pushd /mnt/d/comfy; mkdir -p custom_nodes.bak; for f in (ls -1 /mnt/d/comfy/custom_nodes | grep -v ComfyUI_DimensionWalker); mv ./custom_nodes/$f ./custom_nodes.bak/; end; popd; 
end
