function no_solo_dimensionwalker
 pushd /mnt/d/comfy; mkdir -p custom_nodes.bak; for f in (ls -1 /mnt/d/comfy/custom_nodes.bak); mv ./custom_nodes.bak/$f ./custom_nodes/; end; popd; 
end
