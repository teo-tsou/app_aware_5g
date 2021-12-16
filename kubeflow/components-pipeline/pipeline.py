import kfp
from kfp import *
import kfp.dsl as dsl


@dsl.pipeline(name='First Pipeline', description='Simple Git Pipeline.')
def first_pipeline():

    # Loads the yaml manifest for each component
    step1 = kfp.components.load_component_from_file('/root/step1.yaml')
    step2 = kfp.components.load_component_from_file('/root/step2.yaml')
    
    # Run download_data task and upload_data task
    comp1 = step1()
    comp2 = step2(comp1.output)

    comp3 = dsl.ContainerOp(
        name='trainer',
        image='ttsourdinis/oai-parser',
        command = ['python3', 'step3.py'],
        pvolumes={"/mnt": dsl.PipelineVolume(pvc="kubeflow-pvc")},
        arguments=["--data_x", comp2.outputs['Array_x'], "--data_y", comp2.outputs['Array_y'],]
   )


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(first_pipeline, 'app-aware-pipeline.yaml')

